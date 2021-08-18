from __future__ import print_function
import argparse
import tensorflow as tf

def hello(n):
    var = tf.constant("Hi " + n + ", you printed your name using AI")
    return tf.print(var)

def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument("Name", help="Enter tensorflow greeting")
    args = parser.parse_args()
    result = hello(args.great)
    print(result)

if __name__ == '__main__':
    Main()
