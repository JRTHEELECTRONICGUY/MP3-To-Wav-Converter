import os
from tkinter import Tk, Button, Label, filedialog, messagebox
from pydub import AudioSegment

class MP3ToWAVConverter:
    def __init__(self, master):
        self.master = master
        master.title("MP3 to WAV Converter")
        master.geometry("300x200")

        self.label = Label(master, text="Select an MP3 file to convert to WAV:")
        self.label.pack(pady=10)

        self.select_button = Button(master, text="Select MP3 File", command=self.select_file)
        self.select_button.pack(pady=10)

        self.convert_button = Button(master, text="Convert to WAV", command=self.convert_file)
        self.convert_button.pack(pady=10)
        self.convert_button.config(state="disabled")

        self.selected_file = None

    def select_file(self):
        self.selected_file = filedialog.askopenfilename(
            title="Select an MP3 file",
            filetypes=[("MP3 Files", "*.mp3")]
        )
        if self.selected_file:
            self.label.config(text=f"Selected file: {os.path.basename(self.selected_file)}")
            self.convert_button.config(state="normal")

    def convert_file(self):
        if not self.selected_file:
            messagebox.showerror("Error", "No file selected!")
            return

        wav_file_path = self.selected_file.replace('.mp3', '.wav')
        
        try:
            audio = AudioSegment.from_mp3(self.selected_file)
            audio.export(wav_file_path, format='wav')
            messagebox.showinfo("Success", f"Converted to {wav_file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Error converting file: {e}")

if __name__ == "__main__":
    root = Tk()
    app = MP3ToWAVConverter(root)
    root.mainloop()
