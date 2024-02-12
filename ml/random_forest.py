from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix, precision_score, recall_score, f1_score
import socket
import struct
import pandas as pd

class RandomForest:
    def __init__(self):
        # Loading the dataset into a dataframe and selecting the important columns
        self.routerDF = pd.read_csv('/Users/andrei-r.ionescu/Desktop/MLLICENTA/PyCharmEnvironment/AnomalyDetectionInNetworkTraffic/ml/Prototip5200.csv')
        self.selected_columns = ['No', 'Time', 'Source', 'Destination', 'Protocol', 'Length', 'Info', 'cat']
        self.routerDF = self.routerDF[self.selected_columns]

    def print_routerDF(self):   # Method to display dataframe
        print(self.routerDF)

    def training(self):   # Methos for training, testing and evaluating the Random Forest
        # encoding
        label_encoders = {}
        for column in ['Source', 'Destination', 'Protocol', 'Info', 'cat']:
            encoder = LabelEncoder()
            self.routerDF[column] = encoder.fit_transform(self.routerDF[column])
            label_encoders[column] = encoder

        # drop the 'No' column
        self.routerDF.drop(columns=['No'], errors='ignore', inplace=True)

        # drop the 'Time' column
        self.routerDF.drop(columns=['Time'], errors='ignore', inplace=True)



