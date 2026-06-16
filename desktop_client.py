import tkinter as tk
from tkinter import scrolledtext
import customtkinter as ctk
import socketio
import threading
from datetime import datetime

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class TelegramMessenger(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("PyTelegram Desktop")
        self.geometry("1000x700")
        
        self.sio = socketio.Client()
        self.username = "User"
        self.current_room = "general"
        
        self.setup_ui()
        self.setup_socket()
        
    def setup_ui(self):
        self.sidebar = ctk.CTkFrame(self, width=250)
        self.sidebar.pack(side="left", fill="y")
        
        ctk.CTkLabel(self.sidebar, text="PyTelegram", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=20)
        
        rooms = ["General", "Work", "Random", "Friends"]
        for room in rooms:
            btn = ctk.CTkButton(self.sidebar, text=room, command=lambda r=room.lower(): self.switch_room(r))
            btn.pack(pady=5, padx=20, fill="x")
        
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(side="right", fill="both", expand=True)
        
        self.header = ctk.CTkLabel(self.main_frame, text="General", font=ctk.CTkFont(size=18))
        self.header.pack(pady=10)
        
        self.chat_area = scrolledtext.ScrolledText(self.main_frame, wrap=tk.WORD, bg="#1a1a1a", fg="white")
        self.chat_area.pack(fill="both", expand=True, padx=10, pady=10)
        
        input_frame = ctk.CTkFrame(self.main_frame)
        input_frame.pack(fill="x", padx=10, pady=10)
        
        self.message_entry = ctk.CTkEntry(input_frame, placeholder_text="Type a message...")
        self.message_entry.pack(side="left", fill="x", expand=True, padx=(0,10))
        self.message_entry.bind("<Return>", self.send_message)
        
        send_btn = ctk.CTkButton(input_frame, text="Send", width=80, command=self.send_message)
        send_btn.pack(side="right")
        
    def setup_socket(self):
        @self.sio.event
        def connect():
            print("Connected")
            self.sio.emit('join', {'room': self.current_room})
        
        @self.sio.event
        def receive_message(data):
            self.add_message(data)
        
        threading.Thread(target=self.connect_socket, daemon=True).start()
    
    def connect_socket(self):
        try:
            self.sio.connect('http://localhost:5000')
        except Exception as e:
            print(e)
    
    def switch_room(self, room):
        self.current_room = room
        self.header.configure(text=room.capitalize())
        self.chat_area.delete(1.0, tk.END)
    
    def send_message(self, event=None):
        msg = self.message_entry.get().strip()
        if msg:
            self.sio.emit('send_message', {
                'username': self.username,
                'message': msg,
                'room': self.current_room
            })
            self.message_entry.delete(0, tk.END)
            
    def add_message(self, data):
        timestamp = datetime.now().strftime("%H:%M")
        msg = f"[{timestamp}] {data.get('username', 'Unknown')}: {data.get('message', '')}\n"
        self.chat_area.insert(tk.END, msg)
        self.chat_area.see(tk.END)

if __name__ == "__main__":
    app = TelegramMessenger()
    app.mainloop()