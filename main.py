from utils import extract_metadata

image_path = "test_image.jpg"  # استبدل بالمسار الخاص بالصورة
metadata = extract_metadata(image_path)
for key, value in metadata.items():
    print(f"{key}: {value}")
from utils import detect_edges

image_path = "test_image.jpg"
output_path = detect_edges(image_path)
print(f"Edges saved to: {output_path}")
from utils import generate_report

metadata = {"Camera": "Nikon D750", "Date": "2024:11:20"}
analysis_results = ["Edges detected successfully", "No significant tampering found"]

report_path = generate_report(metadata, analysis_results)
print(f"Report saved to: {report_path}")
import tkinter as tk
from tkinter import filedialog, messagebox
from utils import extract_metadata, detect_edges, generate_report

def analyze_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.png")])
    if not file_path:
        return

    metadata = extract_metadata(file_path)
    edges_path = detect_edges(file_path)
    report_path = generate_report(metadata, ["Edges detected successfully"], "Forgery_Report.pdf")

    messagebox.showinfo("Analysis Complete", f"Report saved to {report_path}")

root = tk.Tk()
root.title("scan image by @Talal Erhoma / 0917145096")
root.geometry("800x200")

btn = tk.Button(root, text="scan image", command=analyze_image)
btn.pack(pady=50)

root.mainloop()
