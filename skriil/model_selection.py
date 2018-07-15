import random
from skriil.errors import InvalidDataError


class KFold:
    def __init__(self):
        self.blocks_x = []
        self.blocks_y = []
        self.scores = []

    def get_score(self):
        return sum(self.scores) / len(self.scores)

    def get_blocks(self, x, y):
        nums = [i for i in range(0, len(x))]
        for i in range(0, 8):
            block_x = []
            block_y = []
            for j in range(0, int(len(x) / 8 )):
                num = random.choice(nums)
                block_x.append(x[num])
                del x[num]
                block_y.append(y[num])
                del y[num]
                nums.pop()
            self.blocks_x.append(block_x)
            self.blocks_y.append(block_y)

    def get_ordered_blocks(self):
        ordered_blocks_x = []
        ordered_blocks_y = []
        nums = [i for i in range(0, len(self.blocks_x))]
        for i in range(0, 4):
            block_x = []
            block_y = []
            for j in range(0, 2):
                num = random.choice(nums)
                block_x.append(self.blocks_x[num])
                block_y.append(self.blocks_y[num])
                nums.pop()
            ordered_blocks_x.append(block_x)
            ordered_blocks_y.append(block_y)

        self.blocks_x = ordered_blocks_x
        self.blocks_y = ordered_blocks_y

    def arrange_blocks(self):
        arranged_blocks_x = []
        arranged_blocks_y = []
        for block in self.blocks_x:
            block_x = []
            for dataset in block:
                for data in dataset:
                    block_x.append(data)
            arranged_blocks_x.append(block_x)
        for block in self.blocks_y:
            block_y = []
            for dataset in block:
                for data in dataset:
                    block_y.append(data)
            arranged_blocks_y.append(block_y)
        self.blocks_x = arranged_blocks_x
        self.blocks_y = arranged_blocks_y

    def blocks_to_list(self, blocks):
        l = []
        for block in blocks:
            for data in block:
                l.append(data)
        return l

    def cross_val(self, model, x, y):
        for i in range(0, 4):
            self.get_blocks(x, y)
            self.get_ordered_blocks()
            self.arrange_blocks()
            x_train_blocks = self.blocks_x
            y_train_blocks = self.blocks_y

            x_test = x_train_blocks[i]
            del x_train_blocks[i]
            y_test = y_train_blocks[i]
            del y_train_blocks[i]

            x_train = self.blocks_to_list(x_train_blocks)
            y_train = self.blocks_to_list(y_train_blocks)

            model.train(x=x_train, y=y_train)
            self.scores.append(model.score(xs=x_test, ys=y_test))

        return self.get_score()


class TrainTestSplit:
    def __init__(self):
        self.x = []
        self.y = []

    @staticmethod
    def throw_exceptions(x, y):
        if len(x) == 0 or len(y) == 0:
            raise InvalidDataError("x or y parameter is missing!")
        if len(x) != len(y):
            raise InvalidDataError("length of x and y has to be the same!")

    def set_values(self, x, y):
        self.x = x
        self.y = y

    def split(self, x=[], y=[], test_size=0.25):
        self.throw_exceptions(x, y)
        self.set_values(x, y)
        x_train = self.x
        x_test = []
        y_train = self.y
        y_test = []
        nums = [x for x in range(0, len(x_train))]
        for i in range(0, int(len(self.x) * test_size)):
            num = random.choice(nums)
            x_test.append(x_train[num])
            del x_train[num]
            y_test.append(y_train[num])
            del y_train[num]
            nums.pop()

        return x_train, x_test, y_train, y_test

