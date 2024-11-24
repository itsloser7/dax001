from PIL import Image
from PIL.ExifTags import TAGS

def extract_metadata(image_path):
    try:
        image = Image.open(image_path)
        metadata = image._getexif()
        if metadata:
            metadata_dict = {}
            for tag, value in metadata.items():
                tag_name = TAGS.get(tag, tag)
                metadata_dict[tag_name] = value
            return metadata_dict
        else:
            return {"Error": "No metadata found. This image may have been edited or lacks metadata."}
    except Exception as e:
        return {"Error": str(e)}

import cv2

def detect_edges(image_path, output_path="output_edges.jpg"):
    try:
        image = cv2.imread(image_path, cv2.IMREAD_COLOR)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 100, 200)
        cv2.imwrite(output_path, edges)
        return output_path
    except Exception as e:
        return {"Error": str(e)}
from fpdf import FPDF

def generate_report(metadata, analysis_results, output_path="report.pdf"):
    try:
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        pdf.cell(200, 10, txt="Forgery Detection Report", ln=True, align="C")

        pdf.cell(200, 10, txt="Metadata Analysis", ln=True, align="L")
        for key, value in metadata.items():
            pdf.cell(0, 10, txt=f"{key}: {value}", ln=True)

        pdf.cell(200, 10, txt="Analysis Results", ln=True, align="L")
        for result in analysis_results:
            pdf.cell(0, 10, txt=result, ln=True)

        pdf.output(output_path)
        return output_path
    except Exception as e:
        return {"Error": str(e)}
