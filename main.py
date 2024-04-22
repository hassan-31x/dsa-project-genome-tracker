import tkinter as tk
from tkinter import ttk
from tkhtmlview import HTMLLabel
from trie import createTrie, prefixWords

# Function to handle the search button click
def search():
    input_text = entry.get()
    words = prefixWords(trie, input_text)
    html = ''
    for i, word in enumerate(words):
        html += f'<p style="padding: 0"><span style="color: red; padding: 0;">{input_text}</span>{word[len(input_text):]}</p>'

    clear_result()
    
    global result_label
    result_label = HTMLLabel(main_frame, html=html, font=("Helvetica", 12), background="white", padx=10, pady=10)
    result_label.pack(padx=10, fill="both", expand=True)

def clear_result():
    global result_label
    if result_label:
        result_label.pack_forget()
        result_label.destroy()


# Function to handle the start button click
def start():
    intro_frame.pack_forget()
    main_frame.pack()

# Creating the trie from a file
trie = createTrie("genomes.txt")

# Creating the UI
root = tk.Tk()
root.title("Genome Sequence Search")
root.geometry("1000x600")

# Introduction screen
intro_frame = tk.Frame(root)
intro_frame.pack(padx=20, pady=20)

intro_label = tk.Label(intro_frame, text="Welcome to Genome Sequence Search!", font=("Helvetica", 18))
intro_label.pack(pady=20)

start_button = ttk.Button(intro_frame, text="Start", command=start)
start_button.pack()

# Main screen
main_frame = tk.Frame(root)

# Input field
entry = ttk.Entry(main_frame, width=50, font=("Helvetica", 12))
entry.pack(padx=10, pady=10)

# Search button
search_button = ttk.Button(main_frame, text="Search", command=search)
search_button.pack(padx=10, pady=10)

result_label = None

# Packing main frame initially hidden
main_frame.pack_forget()

root.mainloop()
