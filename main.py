"""

Data pipeline 
dataset_utilities.py
    in: -
    out: batch of preprocessed data from hard-coded kaggle-url and predesigned format

1. extract data from kaggle dataset 
2. load batches in memory, keep under 2gb batches
3. preprocess data from chunk
    examine which features are relevant for this portion to later use as input for dnn
4. pass entire batch as input to DNN during training, do for subsequent chunks upto N number of rows.


Neural Network Data Structure 
train_icu.py 
    in: batch of preprocessed data
    out: model weights, training accuracy, loss, STORE MODEL WEIGHTS IN DIRECTORY
test_icu.py 
    in: -
    LOAD MODEL WEIGHTS FROM TRAINED NETWORK DIRECTORY
    out: model test accuracy, model test loss, confusion matrix, roc curve

these are decoupled so user can select which model weights to load without training a model every time

Test whether or not patient that shows up in admissions list becomes an ICU patient.
There is overlap between patients that show up for ew emer., eu observation ,..
ICU admits are more scarce than other types of admits, so training data should reflect this skew. 
It should happen naturally if batches are taken sequentially.

Look into which features can be used as input and design input vector for DNN.

The input data will be a hospital admit, then the classification task will be, "No ICU" or "ICU"

Dataset Structure


"""