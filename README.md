# Detecting Police Lights using Computer Vision and Machine Learning

### Objective
The objective of this research project is to train a machine learning model to detect the emergency lights of police cars in order to determine if they are running. Such a model would aid police cars responding to emergencies by allowing self-driving cars to detect and pull over for police cars that have their emergency lights running.

Python and the [Keras](https://keras.io/) TensorFlow library are used to program the neural network.

### Results

Using a small dataset of only 568 images, the model was able to achieve a validation accuracy of 85%.

![Validation accuracy](https://raw.githubusercontent.com/timothymatson/Senior-Research-Project/master/val_accuracy.png)

![Validation loss](https://raw.githubusercontent.com/timothymatson/Senior-Research-Project/master/val_loss.png)

From the divergence between the validation and training accuracy, it's easy to see that the model is overfitting to the small dataset. More examples will need to be collected to improve the validation accuracy.

Below are examples of the features the model is learning.

![Activation maps](https://raw.githubusercontent.com/timothymatson/Senior-Research-Project/master/activation_maps.png)
