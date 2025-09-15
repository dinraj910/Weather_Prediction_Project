# Weather Prediction Project

![Weather Forecast Banner](https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1350&q=80)

<p align="center">
  <a href="https://colab.research.google.com/github/dinraj910/Weather_Prediction_Project/blob/main/Weather_Project.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
  </a>
</p>

## 🚀 Overview

The **Weather Prediction Project** leverages machine learning to forecast next-day temperatures using historical weather data. This futuristic and modern solution is designed for data scientists, meteorology enthusiasts, and anyone interested in predictive analytics.

- **Tech Stack:** Python, Pandas, Scikit-learn, Matplotlib, Seaborn, Joblib
- **Models Used:** Linear Regression, Random Forest Regressor
- **Features:**
  - Lag-based feature engineering
  - Model evaluation (MAE, RMSE)
  - Interactive visualizations
  - Ready-to-use Jupyter Notebook (Colab compatible)

---

## 📂 Project Structure

```
Weather_Prediction_Project/
│
├── Weather_Project.ipynb        # Main Jupyter Notebook (Colab-ready)
├── weatherHistory.csv           # Main dataset
├── archive/
│   └── weatherHistory.csv       # Backup of dataset
├── models/
│   └── weather_model.pkl        # Trained model (not tracked by git)
├── kaggle.json                  # Kaggle API credentials (if needed)
└── README.md                    # Project documentation
```

---

## 🧑‍💻 Quick Start

1. **Clone the repository:**
   ```bash
   git clone https://github.com/dinraj910/Weather_Prediction_Project.git
   cd Weather_Prediction_Project
   ```
2. **Open the notebook:**
   - [Run in Google Colab](https://colab.research.google.com/github/dinraj910/Weather_Prediction_Project/blob/main/Weather_Project.ipynb)
   - Or open `Weather_Project.ipynb` locally in VS Code/Jupyter
3. **Upload the dataset:**
   - Use the file upload cell in the notebook or place `weatherHistory.csv` in the root directory.
4. **Run all cells:**
   - Follow the notebook for data exploration, feature engineering, model training, and evaluation.

---

## 📊 Example Results

- **Model Performance:**
  - Linear Regression and Random Forest are compared using MAE and RMSE.
- **Visualization:**
  - Actual vs. Predicted temperature plots for easy interpretation.

---

## 🛠️ Key Features

- **Futuristic Data Science Workflow:**
  - Clean, modular, and reproducible code
  - Ready for extension with new models or features
- **Modern Visualizations:**
  - Matplotlib and Seaborn for insightful plots
- **Colab Integration:**
  - One-click badge for instant cloud execution
- **Model Export:**
  - Trained model saved as `weather_model.pkl` (excluded from git)

---

## 🤖 Technologies Used

- Python 3.x
- Pandas, NumPy
- Scikit-learn
- Matplotlib, Seaborn
- Joblib

---

## 🌐 Dataset

- [weatherHistory.csv](https://www.kaggle.com/datasets/muthuj7/weather-dataset) (Kaggle)
- Contains 96,454 rows of hourly weather data (Temperature, Humidity, Wind Speed, Pressure, etc.)

---

## 📈 Future Enhancements

- Add deep learning models (LSTM, GRU)
- Integrate real-time weather API
- Deploy as a web app (Streamlit/FastAPI)
- Hyperparameter tuning and model selection
- Automated ML pipelines

---

## 🤝 Contributing

Contributions are welcome! Please open issues or submit pull requests for improvements, bug fixes, or new features.

---

## 📄 License

This project is licensed under the MIT License.

---

## 🙌 Acknowledgements

- [Kaggle](https://www.kaggle.com/datasets/muthuj7/weather-dataset) for the dataset
- Open-source community for libraries and tools

---

<p align="center">
  <b>Made with ❤️ by dinraj910</b>
</p>
