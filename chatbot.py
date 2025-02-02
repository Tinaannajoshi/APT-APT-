import nltk
import numpy as np
import random
import json
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import SGD
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

# Load training data (You can create a JSON file with more responses)
data = {
    "intents": [
        {
            "tag": "greeting",
            "patterns": ["Hello", "Hi", "Hey there"],
            "responses": ["Hello! How can I help you today?", "Hi there! How's your day going?"]
        },
        {
            "tag": "stress",
            "patterns": ["I'm stressed", "Feeling anxious", "I'm worried"],
            "responses": ["I understand. Try taking deep breaths and relaxing for a moment.", "Would you like some stress management tips?"]
        },
        {
            "tag": "study",
            "patterns": ["How to study better?", "Give me study tips"],
            "responses": ["Stay organized, take breaks, and review notes regularly!", "Have you tried using the Pomodoro technique?"]
        },
        {
            "tag": "goodbye",
            "patterns": ["Bye", "See you later"],
            "responses": ["Goodbye! Take care!", "See you soon! Stay positive!"]
        }
    ]
}

# Preprocess the data
words = []
classes = []
documents = []
ignore_words = ["?", "!", ".", ","]

for intent in data["intents"]:
    for pattern in intent["patterns"]:
        word_list = nltk.word_tokenize(pattern)
        words.extend(word_list)
        documents.append((word_list, intent["tag"]))
        if intent["tag"] not in classes:
            classes.append(intent["tag"])

words = sorted(set([lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore_words]))
classes = sorted(set(classes))

# Prepare training data
training = []
output_empty = [0] * len(classes)

for doc in documents:
    bag = []
    word_patterns = [lemmatizer.lemmatize(w.lower()) for w in doc[0]]
    for w in words:
        bag.append(1 if w in word_patterns else 0)
    
    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1
    training.append([bag, output_row])

random.shuffle(training)
train_x = np.array([x[0] for x in training])
train_y = np.array([x[1] for x in training])

# Create a neural network model
model = Sequential([
    Dense(128, input_shape=(len(train_x[0]),), activation="relu"),
    Dense(64, activation="relu"),
    Dense(len(classes), activation="softmax")
])

model.compile(loss="categorical_crossentropy", optimizer=SGD(learning_rate=0.01), metrics=["accuracy"])
model.fit(train_x, train_y, epochs=200, batch_size=5, verbose=1)
model.save("chatbot_model.h5")

print("Training completed and model saved!")