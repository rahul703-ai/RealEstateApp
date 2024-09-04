
---

# Real Estate Price Prediction and Recommendation System Using Machine Learning

## Overview
This project is an end-to-end real estate analytics platform designed to predict property prices and provide recommendations. It uses machine learning algorithms to deliver accurate price predictions and leverages AWS for deployment, ensuring scalability and reliability. The platform includes interactive visualizations and a recommendation system to enhance user experience.

## Features
- **Price Prediction**: Predict property prices using a Random Forest Regressor model with a 90% R² score.
- **Data Visualizations**: Interactive visualizations such as geo maps, amenities word clouds, and scatter plots.
- **Recommendation System**: Suggests similar societies based on user preferences using cosine similarity.
- **Scalable Deployment**: Hosted on AWS for high availability and seamless performance.

## Repositories

### 1. [RealEstateML](https://github.com/rahul703-ai/RealEstateML)
- Contains all datasets and analysis code.
- Includes Jupyter notebooks and scripts for data preprocessing, feature engineering, and model development.

### 2. [RealEstateApp](https://github.com/rahul703-ai/RealEstateApp)
- Contains the Streamlit application code.
- Developed in a PyCharm environment.
- Includes the deployment scripts and code for the web application.

## Installation

### Prerequisites
- Python 3.7+
- pip
- AWS account

### Steps

1. **Clone the RealEstateApp repository**
   ```bash
   git clone https://github.com/rahul703-ai/RealEstateApp.git
   cd RealEstateApp
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application locally**
   ```bash
   streamlit run app.py
   ```

4. **Deploy on AWS**
   - Follow the AWS deployment guide to set up your environment and deploy the app.

## Usage
1. **Predict Prices**: Enter property details to predict prices for flats and houses.
2. **View Analytics**: Explore geo maps, word clouds, and scatter plots for market insights.
3. **Get Recommendations**: Choose a society to get recommendations for similar societies.

## Technologies Used
- **Python**
- **scikit-learn**
- **Streamlit**
- **AWS**
- **Pandas, NumPy**
- **Web Scraping**

## Contributing
Feel free to fork these repositories and submit pull requests. Contributions are welcome!

## License
This project is licensed under the MIT License.

---

