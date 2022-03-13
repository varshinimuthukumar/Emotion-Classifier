from tabnanny import verbose
import audb
import opensmile
from sklearn import preprocessing

def get_data():
    '''
    Function to get the basic emodb data loaded directly from audb package.  

    Input- None
    Output - pandas dataframe returning basic data containing(file, emotion, emotion.confidence)
    '''
    db= audb.load('eodb', version='1.1.1', verbose=True)
    df=db['emotion'].get()
    return df


def extract_audio_features(audio_file):
    '''
    Function to extract feature set on audio files (no input as of now, only extract the FeatureSet.ComParE_2016 features)

    Input-audio file path
    Output- features list extracted by processing the audio file
    '''

    smile = opensmile.Smile(
    feature_set=opensmile.FeatureSet.ComParE_2016,
    feature_level=opensmile.FeatureLevel.Functionals)

    features = smile.process_file(audio_file)

    return features

class dataclass():

    def __init__(self, data ) -> None:
        self.data =  data
        return
    def normalize(self):
        self.data = preprocessing.scale(self.data)
        return
    def get_data(self):
        return self.data    
