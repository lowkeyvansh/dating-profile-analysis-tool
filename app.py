import tkinter as tk
from tkinter import messagebox
from textblob import TextBlob
import re

def setup_window():
    root = tk.Tk()
    root.title("Dating Profile Analysis Tool")
    root.geometry("600x400")
    return root

def create_input_fields(root):
    tk.Label(root, text="Enter profile text:").pack(pady=5)
    profile_entry = tk.Text(root, height=10, width=70)
    profile_entry.pack(pady=5)
    return profile_entry

def create_buttons(root, analyze_profile):
    analyze_button = tk.Button(root, text="Analyze Profile", command=analyze_profile)
    analyze_button.pack(pady=10)
    return analyze_button

def get_profile_text(profile_entry):
    return profile_entry.get("1.0", tk.END).strip()

def analyze_text(profile_text):
    blob = TextBlob(profile_text)
    sentiment = blob.sentiment

    # Extracting keywords (nouns)
    nouns = blob.noun_phrases

    # Counting word frequency
    words = re.findall(r'\w+', profile_text.lower())
    word_freq = {}
    for word in words:
        if word not in word_freq:
            word_freq[word] = 1
        else:
            word_freq[word] += 1

    sorted_word_freq = sorted(word_freq.items(), key=lambda item: item[1], reverse=True)

    return sentiment, nouns, sorted_word_freq

def display_results(root, sentiment, nouns, word_freq):
    result_text = f"Sentiment Analysis:\n\nPolarity: {sentiment.polarity:.2f}\nSubjectivity: {sentiment.subjectivity:.2f}\n\n"
    result_text += "Keywords:\n" + ", ".join(nouns) + "\n\n"
    result_text += "Word Frequency:\n"
    for word, freq in word_freq[:10]:
        result_text += f"{word}: {freq}\n"

    result_window = tk.Toplevel(root)
    result_window.title("Analysis Results")
    result_window.geometry("400x400")
    tk.Label(result_window, text=result_text, justify=tk.LEFT, padx=10, pady=10).pack()

def main():
    root = setup_window()
    profile_entry = create_input_fields(root)
    
    def analyze_profile():
        profile_text = get_profile_text(profile_entry)
        if not profile_text:
            messagebox.showwarning("Input Error", "Please enter profile text.")
            return
        
        sentiment, nouns, word_freq = analyze_text(profile_text)
        display_results(root, sentiment, nouns, word_freq)

    create_buttons(root, analyze_profile)
    root.mainloop()

if __name__ == "__main__":
    main()
