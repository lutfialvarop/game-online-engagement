import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Load Model, Scaler, dan Kolom Fitur
model = joblib.load('xgboost_best_model.pkl')
scaler = joblib.load('scaler.pkl')
feature_columns = joblib.load('feature_columns.pkl')

st.title("🎮 Online Gaming Engagement Predictor")

# --- INPUT USER ---
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", min_value=15, max_value=100, value=25)
    gender = st.selectbox("Gender", ["Male", "Female"])
    location = st.selectbox("Location", ["USA", "Europe", "Asia", "Other"])
    game_genre = st.selectbox("Game Genre", ["Action", "Strategy", "Sports", "Simulation", "RPG"])
    play_time = st.number_input("Play Time (Hours)", min_value=0.0, value=10.0)

with col2:
    in_game_purchases = st.selectbox("In Game Purchases?", ["No", "Yes"])
    game_difficulty = st.selectbox("Game Difficulty", ["Easy", "Medium", "Hard"])
    sessions_per_week = st.number_input("Sessions Per Week", min_value=0, value=5)
    avg_session_duration = st.number_input("Avg Session Duration (Minutes)", min_value=0, value=60)
    player_level = st.number_input("Player Level", min_value=0, value=10)
    achievements = st.number_input("Achievements Unlocked", min_value=0, value=5)

# --- PREPROCESSING ---
if st.button("Predict Engagement"):
    # 1. Mapping Data Manual (Sesuai Notebook)
    purchases_map = {"No": 0, "Yes": 1}
    difficulty_map = {"Easy": 0, "Medium": 1, "Hard": 2}
    
    # 2. Buat DataFrame awal dengan nilai 0 untuk semua kolom
    # Ini trik agar One-Hot Encoding tidak error jika ada kategori yang hilang
    input_data = pd.DataFrame(np.zeros((1, len(feature_columns))), columns=feature_columns)
    
    # 3. Isi Data Numerik
    input_data['Age'] = age
    input_data['PlayTimeHours'] = play_time
    input_data['InGamePurchases'] = purchases_map[in_game_purchases]
    input_data['SessionsPerWeek'] = sessions_per_week
    input_data['AvgSessionDurationMinutes'] = avg_session_duration
    input_data['PlayerLevel'] = player_level
    input_data['AchievementsUnlocked'] = achievements
    input_data['GameDifficulty'] = difficulty_map[game_difficulty]
    
    # 4. Isi Data Kategorikal (One-Hot Encoding Manual)
    # Set kolom one-hot menjadi 1 jika sesuai pilihan user
    if f"Gender_{gender}" in input_data.columns:
        input_data[f"Gender_{gender}"] = 1
        
    if f"Location_{location}" in input_data.columns:
        input_data[f"Location_{location}"] = 1
        
    if f"GameGenre_{game_genre}" in input_data.columns:
        input_data[f"GameGenre_{game_genre}"] = 1
    
    # 5. Scaling (Wajib dilakukan karena saat training pakai StandardScaler)
    # Kolom numerik yang harus di-scale (sesuai notebook)
    num_cols = ["Age", "PlayTimeHours", "InGamePurchases", "SessionsPerWeek",
                "AvgSessionDurationMinutes", "PlayerLevel", "AchievementsUnlocked"]
    
    input_data[num_cols] = scaler.transform(input_data[num_cols])
    
    # --- PREDIKSI ---
    prediction = model.predict(input_data)[0]
    
    # Mapping hasil prediksi kembali ke label
    label_map = {0: "Low", 1: "Medium", 2: "High"}
    result = label_map.get(prediction, "Unknown")
    
    # Tampilkan Hasil
    if result == "High":
        st.success(f"Engagement Level: **{result}** 🚀")
    elif result == "Medium":
        st.info(f"Engagement Level: **{result}** ⚖️")
    else:
        st.warning(f"Engagement Level: **{result}** 📉")