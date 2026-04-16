# Aerial Image Classification (Bird vs Drone) using Deep Learning

## 📌 Overview

This project implements a deep learning-based system to classify aerial images into **Bird** and **Drone** categories. Two approaches were used: a custom Convolutional Neural Network (CNN) and a transfer learning model (MobileNetV2). The final model is deployed using Streamlit for real-time predictions.

---

## 🚀 Features

* Image classification using Deep Learning
* Comparison between CNN and Transfer Learning
* Achieved **~95% accuracy** using MobileNetV2
* Data augmentation for improved generalization
* Streamlit-based web application for real-time predictions

---

## 🧠 Models Used

### 🔹 Custom CNN

* Accuracy: ~85%
* Moderate training time
* Slight overfitting observed

### 🔹 MobileNetV2 (Transfer Learning)

* Accuracy: ~95.35%
* Faster training
* Better generalization

---

## 📊 Results

### Accuracy Graph

![Accuracy](images/accuracy_graph.png)

### Streamlit Output

![Streamlit](images/streamlit_output.png)

---

## 🧪 Evaluation

* Confusion Matrix
* Precision, Recall, F1-score
* Model comparison analysis

---

## ▶️ How to Run

1. Clone the repository:

```bash
git clone https://github.com/hubsukalp/Aerial-Image-Classification-Bird-vs-Drone.git
```

2. Navigate to project folder:

```bash
cd Aerial-Image-Classification-Bird-vs-Drone
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the Streamlit app:

```bash
streamlit run app.py
```

---

## 📂 Dataset

Dataset used for classification:
https://drive.google.com/drive/folders/1nn1vqsh8juhafkJcleembrjQ9EqtIoMh?usp=sharing


---

## 📁 Project Structure

```
Aerial-Image-Classification-Bird-vs-Drone/
│── app.py
│── best_model.keras
│── cnn_model.keras (optional)
│── Aerial_Image_Classification_Bird_vs_Drone.ipynb
│── requirements.txt
│── images/
```

---

## ⚙️ Tech Stack

* Python
* TensorFlow / Keras
* Streamlit
* NumPy, Matplotlib
* Scikit-learn

---

## 🔮 Future Scope

* Implement object detection using YOLOv8
* Extend to real-time video surveillance
* Deploy on cloud platforms

---

## 👨‍💻 Author

**Sukalp Warhekar**

---

## 🔗 Project Repository

GitHub Link: https://github.com/hubsukalp/Aerial-Image-Classification-Bird-vs-Drone
