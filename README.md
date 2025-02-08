# 🎮 Ball Dropping and Catching Game (Computer Vision + Pygame)

This is a **fun and interactive ball-catching game** that uses **Computer Vision (OpenCV & Mediapipe)** to track hand movements and control a paddle in **Pygame**. The objective is to **catch the falling balls** before they hit the ground. Each time you catch a ball, a new one appears, and its speed increases, making the game progressively more challenging! 🚀

---

## 📌 Features

✅ **Hand-tracking-based Paddle Movement** using OpenCV & Mediapipe  
✅ **Dynamic Ball Speed** – The ball falls faster as your score increases  
✅ **New Ball Appears After Each Catch** – Only one ball at a time per horizontal lane  
✅ **Game Over if a Ball is Missed**  
✅ **"Play Again" Option** (Press `SPACE` to restart, `Q` to quit)  

---

## 🛠 Installation

### **1️⃣ Clone this repository**
```bash
git clone https://github.com/YourGitHubUsername/Ball-Dropping-Game.git
```
### **2️⃣ Navigate to the project folder**
```bash
cd Ball-Dropping-Game
```
### **3️⃣ Install Dependencies**
```bash
pip install opencv-python mediapipe pygame
```
### **4️⃣ Run the Game**
```bash
python ball_game.py
```

## 🎮 How to Play
1️⃣ **Move your hand in front of the camera** 📷 to control the paddle.  
2️⃣ **Catch the falling ball** with the paddle.  
3️⃣ **Each time you catch a ball, a new one appears, and its speed increases.**  
4️⃣ **If you miss a ball, the game ends.**  
5️⃣ **Press `SPACE` to play again or `Q` to quit.**  

---

## 📷 Hand Tracking Setup
The game uses **Mediapipe's Hand Tracking** to detect your hand position and move the paddle accordingly.

### **Hand Movement Controls**
- 🖐 **Move your hand left or right** → Paddle moves left or right  
- ⚡ **No need for keyboard/mouse!**  

---

## 🖼 Game Screenshot

Below is a screenshot of the game in action:

![Game Screenshot](Screenshot%202025-02-08%20172525.png)

---

## 🚀 Future Enhancements
- 🎵 Add sound effects for catching and missing balls  
- 🔥 Implement multiple difficulty levels (Easy, Medium, Hard)  
- 🏆 Add a High Score system  

---

## 📜 License
This project is open-source and free to use under the **MIT License**.  

---

## 💡 Credits
👨‍💻 **Created by:** Your Name  
🎮 **Inspired by:** AI-based gaming and Computer Vision  

---

⭐ **If you like this project, feel free to give it a star!** ⭐  
