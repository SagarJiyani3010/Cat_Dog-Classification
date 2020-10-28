import os
import random
from shutil import copyfile


def split_data(Source, Training, Testing, Split_size):
    files = []
    for filename in os.listdir(Source):
        file = Source + filename
        if os.path.getsize(file) > 0:
            files.append(filename)
        else:
            print(filename + ' is zero length, so ignoring.')

    training_length = int(len(files) * Split_size)
    testing_length = int(len(files) - training_length)
    shuffled_set = random.sample(files, len(files))
    training_set = shuffled_set[0:training_length]
    testing_set = shuffled_set[-testing_length:]

    for filename in training_set:
        this_file = Source + filename
        destination = Training + filename
        copyfile(this_file, destination)

    for filename in testing_set:
        this_file = Source + filename
        destination = Testing + filename
        copyfile(this_file, destination)


if __name__ == "__main__":

    DATA_DIR = '../input/'
    cats = os.path.join(DATA_DIR, 'Cat/')
    dogs = os.path.join(DATA_DIR, 'Dog/')

    try:
        os.mkdir('../dataset')
        os.mkdir('../dataset/training')
        os.mkdir('../dataset/testing')
        os.mkdir('../dataset/training/dogs')
        os.mkdir('../dataset/testing/cats')
        os.mkdir('../dataset/testing/dogs')
        os.mkdir('../dataset/training/cats')
    except OSError:
        pass

    cat = os.path.join(DATA_DIR, 'Cat/')
    dog = os.path.join(DATA_DIR, 'Dog/')
    cat_train = os.path.join('../dataset/training/cats/')
    cat_test = os.path.join('../dataset/testing/cats/')
    dog_train = os.path.join('../dataset/training/dogs/')
    dog_test = os.path.join('../dataset/testing/dogs/')

    split_data(cat, cat_train, cat_test, 0.85)
    split_data(dog, dog_train, dog_test, 0.85)
