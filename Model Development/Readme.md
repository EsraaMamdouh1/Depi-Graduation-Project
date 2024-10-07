<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>

<h1>Stress Detection using LSTM Networks</h1>

<p>This project leverages Long Short-Term Memory (LSTM) networks to detect stress levels using EEG and ECG data. The model is designed to handle sequential time-series data and classify whether the subject is under stress or not. The development is guided by principles of deep learning and signal processing, with an emphasis on model accuracy and generalization.</p>

<h2>Table of Contents</h2>
<ul>
    <li><a href="#overview">Overview</a></li>
    <li><a href="#model">Model Architecture</a></li>
    <li><a href="#why">Why LSTM?</a></li>
    <li><a href="#data">Data Preprocessing</a></li>
    <li><a href="#training">Training & Evaluation</a></li>
    <li><a href="#results">Results</a></li>
    <li><a href="#requirements">System Requirements</a></li>
    <li><a href="#usage">Usage Instructions</a></li>
    <li><a href="#future">Future Directions</a></li>
    <li><a href="#contributors">Contributors</a></li>
</ul>

<h2 id="overview">Overview</h2>

<p>This project aims to develop a robust system that identifies stress levels by analyzing physiological signals, specifically EEG and ECG. The system employs a binary classification approach to predict stress conditions, leveraging deep learning architectures tailored for time-series data.</p>

<h2 id="model">Model Architecture</h2>

<p>The LSTM-based model is built with the following components:</p>
<ul>
    <li><strong>LSTM Layers:</strong> Extract sequential patterns from the data, using both temporal dependencies and context.</li>
    <li><strong>Dense Layers:</strong> Fully connected layers that process the extracted features into condensed representations for final predictions.</li>
    <li><strong>Dropout Layers:</strong> Implemented after key layers to reduce overfitting by deactivating random neurons during training.</li>
    <li><strong>Output Layer:</strong> A sigmoid function produces the binary stress classification.</li>
    <li><strong>Adam Optimizer:</strong> With a learning rate of 0.0003, it optimizes the network's weights, and gradient clipping is applied for training stability.</li>
</ul>

<h3>Key Layer Specifications:</h3>
<code>
LSTM(128 units, return_sequences=True) → Dropout(50%) → LSTM(64 units) → Dense(128 units, ReLU) → Dropout(40%) → Dense(64 units) → Sigmoid Output Layer
</code>

<h2 id="why">Why LSTM?</h2>

<p>EEG and ECG data are inherently time-dependent, and LSTMs are designed to address the challenges of sequential data processing. LSTM networks can preserve important information across long sequences, making them superior to traditional feed-forward neural networks for this type of task. Additionally, LSTMs effectively mitigate the vanishing gradient problem, ensuring stable and reliable training.</p>

<h2 id="data">Data Preprocessing</h2>

<p>Given the nature of EEG and ECG data, several preprocessing steps were applied:</p>
<ul>
    <li><strong>Feature Selection:</strong> Recursive Feature Elimination (RFE) was used to identify the most relevant signals.</li>
    <li><strong>Normalization:</strong> Data was normalized to ensure consistency across different input features.</li>
    <li><strong>Sequence Reshaping:</strong> Data was reshaped into sequences to align with the LSTM’s input format.</li>
</ul>

<h2 id="training">Training & Evaluation</h2>

<p>To optimize the model's performance, the following training setup was employed:</p>
<ul>
    <li><strong>Epochs:</strong> 150</li>
    <li><strong>Batch Size:</strong> 16</li>
    <li><strong>Loss Function:</strong> Binary Cross-Entropy</li>
    <li><strong>Metrics:</strong> Accuracy and F1 Score</ul>

<h3>Training Callbacks:</h3>
<ul>
    <li><strong>ReduceLROnPlateau:</strong> Dynamically reduces the learning rate when the validation loss plateaus.</li>
    <li><strong>EarlyStopping:</strong> Stops training when no improvements are seen for 10 consecutive epochs, restoring the best model weights.</li>
</ul>

<h2 id="results">Results</h2>

<p>The model’s performance was evaluated using accuracy and F1 score. Each model was trained and evaluated separately for both male and female subjects across different activity states (e.g., EO, AC1). These results demonstrate the model's effectiveness in detecting stress patterns from physiological signals.</p>

<h2 id="requirements">System Requirements</h2>

<p>To run this project, ensure the following dependencies are installed:</p>
<ul>
    <li>Python 3.x</li>
    <li>TensorFlow 2.x</li>
    <li>NumPy</li>
    <li>Pandas</li>
    <li>Scikit-learn</li>
    <li>Matplotlib (optional, for data visualization)</li>
</ul>

<p>Install the required packages via:</p>
<code>pip install -r requirements.txt</code>

<h2 id="usage">Usage Instructions</h2>

<p>Clone the repository and execute the model training script:</p>
<code>git clone https://github.com/AbdelrahmanAboegela/Depi-Graduation-Project.git</code>
<br>
<code>python train_model.py</code>

<p>The script handles the data split into training and validation sets and applies callbacks for learning rate scheduling and early stopping based on validation loss.</p>

<h2 id="future">Future Directions</h2>

<p>There are several areas for future exploration:</p>
<ul>
    <li>Implementing more advanced neural architectures such as Gated Recurrent Units (GRU) or combining LSTM with Convolutional Neural Networks (CNNs).</li>
    <li>Expanding the model to handle real-time stress detection using live EEG/ECG streams.</li>
    <li>Improving model generalization through larger and more diverse datasets.</li>
    <li>Exploring multi-class classification to detect different levels of stress severity.</li>
</ul>

<h2 id="contributors">Contributors</h2>

<p><strong><a href="https://github.com/AbdelrahmanAboegela">Abdelrahman Aboegela</a></strong></p>
<p><strong><a href="https://github.com/TasnemMahmoud">Tasnem Mahmoud</a></strong></p>

</body>
</html>
