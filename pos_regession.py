#daten einlesen
def read_data(train_datapath):  
    all_sentences = []
    with open(train_datapath, 'r') as infile:
        sentence = []
        for line in infile:
            line = str.split(str.strip(line), '\t')
            if len(line) == 3:
                token, tag_label= line[0], line[2]
                sentence.append((token, tag_label))
        all_sentences.append(sentence)
        sentence = []
    return all_sentences
    
#x und y splitten
def form_data(all_sentences):
    """Create dataset"""
    features   = []                                                     # This is our x_train
    pos_labels = []                                                     # This is our y_train
    for sent in all_sentences:
        for token_index, token_pair in enumerate(sent):
            token       = token_pair[0]                                 # Get token
            features.append(get_feature(token, token_index, sent)) # Extract features from token and append it to features list (x_train)
            pos_label = token_pair[1]                                   # Get ground truth (golden) pos label of token
            pos_labels.append({'tag':pos_label})                                # Append pos label to pos_labels list (y_train) 

    return features, pos_labels                                         #Return x_train and y_train

def get_feature(token, token_index, sent):
    """Extract features of given word(token)"""
    token_feature = {    
        'token'             : token#,                                    # Token itself
       }
    return  token_feature
    
    
    
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegressionCV

from sklearn.linear_model import LogisticRegression


from sklearn.metrics import accuracy_score
from sklearn.preprocessing  import LabelEncoder
import numpy as np   
from keras.models import Sequential
from keras.layers import Flatten,Dropout, Activation,Dense, LSTM, InputLayer, Bidirectional, TimeDistributed, Embedding
from tensorflow.keras.optimizers import Adam
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split


#vector initialisieren
vectorizer = DictVectorizer()                               # Initialize dictionary vectorizer
#modell inizialisieren 
model = Sequential()


#daten einlesen
datapath = 'en-ud-dev(1).conllu'
all_sentence            = read_data(datapath)                               # Read sentences from test data
#x und y splitten
features, labels = form_data(all_sentence)


#x vektorisieren
vectorizer.fit(features)                                                    # Train vectorizer
vectorized_features = vectorizer.transform(features)



print(vectorizer.get_feature_names_out())                                                   # Convert features from dictionary form to vector form
print(vectorized_features.toarray())       
#y vektorisieren
vectorizer.fit(labels)
vectorized_labels= vectorizer.transform(labels)  

print(vectorizer.get_feature_names_out())                                                   # Convert features from dictionary form to vector form
print(vectorized_labels.toarray())                                                   # Convert features from dictionary form to vector form
print(features)
print(labels)


#test und train splitten
X_train, X_test, y_train, y_test = train_test_split(vectorized_features.toarray(), vectorized_labels.toarray(), test_size=.2, random_state=777)

print(vectorized_features.toarray().shape)

print(vectorized_labels.toarray().shape)
#layer für modell hinzufügen
model.add(Flatten())
model.add(Dense(960, input_dim=463))


model.add(Dense(100))
model.add(Dropout(0.2))
model.add(Dense(40, activation=('sigmoid')))



model.compile(optimizer=Adam(0.001), loss='categorical_crossentropy', metrics=['acc'])
#modell evaluieren
history=model.fit(X_train, y_train, batch_size=128, epochs=10, validation_data=(X_test,y_test))
model.evaluate(X_test,y_test)[1]
model.summary()








#modell accuracy plotten
epochs = range(1, len(history.history['acc']) + 1)
plt.plot(epochs, history.history['acc'])
plt.plot(epochs, history.history['val_acc'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epochs')
plt.legend(['train', 'test'], loc='lower right')
plt.show()
#modell loss plotten
epochs = range(1, len(history.history['loss']) + 1)
plt.plot(epochs, history.history['loss'])
plt.plot(epochs, history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epochs')
plt.legend(['train', 'test'], loc='upper right')
plt.show()
