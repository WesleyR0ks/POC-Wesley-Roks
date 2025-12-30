import tkinter as tk
from model.predictor import predict_email

def check_email():
    email_text = text_box.get("1.0", tk.END)
    if not email_text.strip():
        result_label.config(text="Please enter an email.", fg="orange")
        return

    try:
        result = predict_email(email_text)
    except Exception as e:
        result_label.config(
            text="An error occurred while analyzing the email. Please try again later.",
            fg="orange",
        )
        return
    color = "red" if result == "PHISHING" else "green"
    result_label.config(text=f"Result: {result}", fg=color)

# Window
window = tk.Tk()
window.title("Phishing Email Detector")
window.geometry("600x400")

label = tk.Label(window, text="Paste email content below:")
label.pack(pady=10)

text_box = tk.Text(window, height=10, width=70)
text_box.pack()

button = tk.Button(window, text="Check Email", command=check_email)
button.pack(pady=10)

result_label = tk.Label(window, text="", font=("Arial", 14))
result_label.pack(pady=10)

window.mainloop()
