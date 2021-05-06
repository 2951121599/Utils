import functools
import numpy as np

np.set_printoptions(precision=3, suppress=True)
import tensorflow as tf

train_file_path = "C:\\Users\\LJD\\Desktop\\ljd\\train.csv"
test_file_path = "C:\\Users\\LJD\\Desktop\\ljd\\test.csv"

LABEL_COLUMN = 'gender'
LABELS = [0, 1]


def get_dataset(file_path):
    dataset = tf.data.experimental.make_csv_dataset(
        file_path,
        batch_size=12,
        label_name=LABEL_COLUMN,
        na_value="?",
        num_epochs=1,
        ignore_errors=True)
    return dataset


raw_train_data = get_dataset(train_file_path)
raw_test_data = get_dataset(test_file_path)

examples, labels = next(iter(raw_train_data))
print("EXAMPLES: \n", examples, "\n")
print("LABELS: \n", labels)

# 以下为数据预处理
CATEGORIES = {
    'gender': ['male', 'female']
}

categorical_columns = [0]
for feature, vocab in CATEGORIES.items():
    cat_col = tf.feature_column.categorical_column_with_vocabulary_list(
        key=feature, vocabulary_list=vocab)
    categorical_columns.append(tf.feature_column.indicator_column(cat_col))

categorical_columns


# 以下为连续数据处理

def process_continuous_data(mean, data):
    data = tf.cast(data, tf.float32) * 1 / (2 * mean)
    return tf.reshape(data, [-1, 1])


MEANS = {
    'gender': 0.5
}

numerical_columns = []

for feature in MEANS.keys():
    num_col = tf.feature_column.numeric_column(
        feature, normalizer_fn=functools.partial(process_continuous_data, MEANS[feature]))
    numerical_columns.append(num_col)

numerical_columns

preprocessing_layer = tf.keras.layers.DenseFeatures(
    categorical_columns + numerical_columns)

model = tf.keras.Sequential([
    preprocessing_layer,
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(16, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid'),
])

model.compile(
    loss='binary_crossentropy',
    optimizer='adam',
    metrics=['accuracy'])

train_data = raw_train_data.shuffle(500)
test_data = raw_test_data

model.fit(train_data, epochs=20)

model.summary()
# 训练完成后，在测试集检查准确性
test_loss, test_accuracy = model.evaluate(test_data)

print()
print(f'Test Loss {test_loss}, Test Accuracy {test_accuracy}')

predictions = model.predict(test_data)
predictions[:10]
list(test_data)[0][1]

for prediction, male in zip(predictions[:10], list(test_data)[0][1][:10]):
    is_male = "male" if bool(male) else "female"
    print(f"预测是男概率: {prediction[0]} | 实际值: {is_male}")
