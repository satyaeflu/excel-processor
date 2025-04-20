import streamlit as st
import openpyxl
from io import BytesIO

# 1. Upload
uploaded_file = st.file_uploader("📤 Upload ANY Excel File")

if uploaded_file:
    try:
        # 2. Process (with obvious visible changes)
        wb = openpyxl.load_workbook(BytesIO(uploaded_file.read()))
        sheet = wb.active
        sheet['A1'] = "👉 I WORKED!"  # Can't-miss change
        sheet['A1'].font = openpyxl.styles.Font(color="FF0000", size=20)
        
        # 3. Download
        output = BytesIO()
        wb.save(output)
        st.download_button(
            "⬇️ DOWNLOAD YOUR FILE",
            data=output.getvalue(),
            file_name="PROOF_IT_WORKED.xlsx"
        )
        st.balloons()  # Celebration!
        
    except Exception as e:
        st.error(f"Oops! {str(e)}")
        st.info("Try this test file first 👇")
        
        # 4. Test File Generator
        wb = openpyxl.Workbook()
        wb.active['A1'] = "TEST PASSED"
        test_file = BytesIO()
        wb.save(test_file)
        
        st.download_button(
            "⬇️ Download TEST FILE",
            data=test_file.getvalue(),
            file_name="TEST_ME.xlsx"
        )