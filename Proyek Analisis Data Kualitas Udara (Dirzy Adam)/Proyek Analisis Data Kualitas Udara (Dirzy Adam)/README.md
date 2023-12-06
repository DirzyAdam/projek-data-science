# 1. Setup Environment
conda create --name main-ds python=3.8
conda activate main-ds
pip install numpy pandas scipy matplotlib seaborn jupyter streamlit babel

# 2. Run Streamlit App
streamlit run "dashboard air quality.py"
