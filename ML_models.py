from sklearn import svm
from sklearn.metrics import confusion_matrix
from sklearn.metrics improt recall_score
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.mixture import GaussianMixture


class GMM_model():
    def __init__(self, n_components=3, covariance_type="diag") -> None:
        self.gm = GaussianMixture(n_components=n_components, covariance_type="diag")

    def fit_model(self, data):
        



        







