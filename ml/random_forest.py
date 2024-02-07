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
        self.routerDF = pd.read_csv('Prototip5200.csv')
        self.selected_columns = ['No', 'Time', 'Source', 'Destination', 'Protocol', 'Length', 'Info', 'cat']
        self.routerDF = self.routerDF[self.selected_columns]

