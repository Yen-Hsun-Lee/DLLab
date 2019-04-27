import tensorflow as tf

constnatTF = tf.constant("Hello Tensorflow!")
session1 = tf.Session()
print(session1.run(constnatTF))