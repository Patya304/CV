from pathlib import Path

import streamlit as st
from PIL import Image
# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Modróczky Patrick"
PAGE_ICON = ":wave:"
NAME = "Modróczky Patrick"
DESCRIPTION = """
Tanuló
"""
EMAIL = "modroczky.patrik@wm-iskola.hul.com"
SOCIAL_MEDIA = {
    "YouTube": "https://youtube.com/@misstren",
    "GitHub": "https://github.com/Patya304",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Önéletrajz leöltése",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("SZAKMAI TAPASZTALAT")
st.write(
    """
- 
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Szakmai képességek")
st.write(
    """
- 👩‍💻 Programozás: Python, HTML, C#
- 🗄️ Adatkezelés: Postgres, MongoDB, MySQL
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Munka előzmények")
st.write("---")

#
st.write("🚧", "**Árufeltöltő**")
st.write("[ 17/06/2022 – 30/08/2022 ]")
st.write(
    """
- [ 17/06/2022 – 30/08/2022 ] 
- vásárlók kisegítése
- árufeltöltés
"""
)

# --- School ---
st.write('\n')
st.subheader("Oktatás és képzés")
st.write("---")

st.write("🚧", "**Érettségi**")
st.write("BKSZC Weiss Manfréd Technikum, Szakképző Iskola és Kollégium [ 01/09/2021 – Jelenlegi ] ")

st.write('\n')
st.subheader("Nyelvtudás")
st.write("---")

st.write("🚧", "**Anyanyelv: Magyar**")
st.write("További nyelvek: Angol")
st.write("Szintek: A1 és A2: Alapszintű nyelvhasználó; B1 és B2: Önálló nyelvhasználó; C1 és C2: Mesterfokú nyelvhasználó")
