# Chatbot - Python Chat Assistant  
google drive link of video demonstration of chatbot task -https://drive.google.com/file/d/1MLWEEsEU8Y1108IKhJXs1t_F2gZq4Al5/view?usp=drive_link

## 📌 Description  
This is a simple chatbot built in Python that responds to user inputs based on predefined commands.  
It supports multiple operations, including list processing, prime number generation, and chat history search.

---

## 🚀 Features  
### ✅ **1. Basic Chat Responses**  
- `hello` / `hi` → Greets the user.  
- `date` / `time` → Displays the current date and time.  
- `bye` → Ends the conversation.  

### ✅ **2. List Operations**  
1. When the user enters `list operations`, the chatbot asks for a **comma-separated list of integers**.  
2. It returns:  
   - **Sum** of the list.  
   - **Maximum** number.  
   - **Reversed list order**.  
3. It then asks if duplicates should be removed. If **"yes"**, it removes duplicates and sorts the list.  

### ✅ **3. Prime Number Generator**  
- If the user enters `generate prime`, the chatbot prompts for a range (`start, end`) and returns all prime numbers in that range.

### ✅ **4. Chat History Search**  
- Users can enter `search history` and input a keyword to find past messages in the conversation.  

### ✅ **5. save as file**  
- the chat history is saved as text file when user enter yes .
---

## 🛠️ Installation & Setup  
1. **Clone the repository**  
   ```bash
   git clone https://github.com/yourusername/chatbot.git
   cd chatbot
   ```
2. **Run the chatbot script**  
   ```bash
   python chatbot.py
   ```

---

## 📌 Example Usage  

### **User Flow (List Operations Example)**  
```plaintext
User: list operations  
Chatbot: Please enter a list of integers (comma-separated, e.g., 5, 12, 7):  
User: 5, 12, 7, 7, 5  
Chatbot:  
  Sum: 36  
  Maximum: 12  
  Reversed List: [5, 7, 7, 12, 5]  
  Would you like to remove duplicates? (yes/no)  
User: yes  
Chatbot: Updated List: [5, 7, 12]  
```

---

## 🔧 Technologies Used  
- **Python**  
- **Datetime module** (for date & time)  

---

## 🤝 Contribution  
Contributions are welcome! Submit a pull request to enhance features.  

---

## 🐜 License  
This project is licensed under the MIT License.  

---

🚀 **Happy Coding!** 😃  
