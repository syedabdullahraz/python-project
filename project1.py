import streamlit as st
import pandas as pd
from io import BytesIO

st.set_page_config(page_title="📁 File Converter & Cleaner", layout="wide")
st.title("📁 File Converter & Cleaner")
st.markdown("Upload CSV or Excel files, clean the data, and download in your desired format.")

files = st.file_uploader("📤 Upload CSV or Excel files", type=["csv", "xlsx"], accept_multiple_files=True)

if files:
    for file in files:
        file_name = file.name
        ext = file_name.split(".")[-1].lower()

        # Read file based on extension
        try:
            df = pd.read_csv(file) if ext == "csv" else pd.read_excel(file)
        except Exception as e:
            st.error(f"Error reading {file_name}: {e}")
            continue

        st.markdown(f"### 🔍 Preview: `{file_name}`")
        st.dataframe(df.head())

        # Duplicates removal
        if st.checkbox(f"🧹 Remove Duplicates - {file_name}"):
            original_rows = len(df)
            df = df.drop_duplicates()
            removed = original_rows - len(df)
            st.success(f"✅ Removed {removed} duplicate rows.")
            st.dataframe(df.head())

        # Fill missing values
        if st.checkbox(f"🧩 Fill Missing Values - {file_name}"):
            numeric_cols = df.select_dtypes(include=['number']).columns
            if not numeric_cols.empty:
                df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                st.success("✅ Missing numeric values filled with column mean.")
            else:
                st.info("ℹ️ No numeric columns found to fill.")
            st.dataframe(df.head())

        # Column selection
        with st.expander(f"🧬 Select Columns - {file_name}", expanded=True):
            selected_columns = st.multiselect("Choose columns to keep:", df.columns.tolist(), default=df.columns.tolist())
            df = df[selected_columns]
            st.dataframe(df.head())

        # Show chart
        numeric_df = df.select_dtypes(include='number')
        if not numeric_df.empty and st.checkbox(f"📊 Show Chart - {file_name}"):
            st.bar_chart(numeric_df.iloc[:, :2])  # Display first 2 numeric columns

        # File conversion
        st.markdown("### 🔁 Convert & Download")
        format_choice = st.radio(f"Choose format for `{file_name}`:", ["CSV", "Excel"], key=f"format_{file_name}")

        if st.button(f"⬇️ Download {file_name} as {format_choice}", key=f"download_{file_name}"):
            output = BytesIO()
            if format_choice == "CSV":
                df.to_csv(output, index=False)
                mime = "text/csv"
                new_name = file_name.rsplit(".", 1)[0] + ".csv"
            else:
                df.to_excel(output, index=False, engine='openpyxl')
                mime = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                new_name = file_name.rsplit(".", 1)[0] + ".xlsx"

            output.seek(0)
            st.download_button("📥 Download File", data=output, file_name=new_name, mime=mime)

st.success("✨ Processing complete!")
