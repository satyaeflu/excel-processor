import streamlit as st
import openpyxl
from io import BytesIO

st.title("📊 My First Excel Processor")

uploaded_file = st.file_uploader("Upload Excel File", type=["xlsx", "xlsm"])

if uploaded_file:
    # Load workbook
    wb = openpyxl.load_workbook(BytesIO(uploaded_file.read()))
    sheet = wb.active
    
    # Simple formatting example
    st.success("Processing...")
    sheet['A1'].font = openpyxl.styles.Font(bold=True, color="FF0000")
    sheet['A1'].value = "Processed with Streamlit"
    
    # Download button
    output = BytesIO()
    wb.save(output)
    st.download_button(
        label="⬇️ Download Modified File",
        data=output.getvalue(),
        file_name="modified_" + uploaded_file.name,
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )