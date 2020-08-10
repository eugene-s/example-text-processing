import fasttext


if __name__ == "__main__":
    model = fasttext.train_supervised("./training_data.txt")
    print(model.words)
    print(model.labels)
    model.test("./testing_data.txt")
    r = model.predict("how to cook some rice")
    print(r)
