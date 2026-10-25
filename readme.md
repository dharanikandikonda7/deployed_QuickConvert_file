# QuickConvert

QuickConvert is a Windows desktop application designed to make everyday file conversion tasks simple through a graphical interface and Windows File Explorer context-menu integration.

## Features

- Convert supported image formats.
- Convert images to PDF.
- Convert PDFs to images or text.
- Convert text files to PDF or HTML.
- Convert HTML files to text.
- Convert DOCX files to text or HTML.
- Convert text files to DOCX.
- Convert DOCX files to PDF.
- Convert PDF files to DOCX.
- Open supported files from the Windows right-click menu when the context-menu integration is installed.

> Available conversions depend on the version of QuickConvert installed. Some document conversions may require additional software on the computer. In particular, DOCX-to-PDF conversion through `docx2pdf` requires Microsoft Word.

## Download and install

1. Download `QuickConvert-Setup.exe` from the QuickConvert website.
2. Run the installer and follow the on-screen instructions.
3. Open QuickConvert from the installed application shortcut, or use the supported Windows right-click menu if configured.

Only download the installer from a source you trust.

## Website

This repository can contain the Streamlit website used to introduce QuickConvert and distribute its Windows installer.

### Website files

- `app.py` — Streamlit landing page.
- `requirements.txt` — Python dependencies required by the website.
- `QuickConvert-Setup.exe` — Windows installer, if you choose to store it alongside the app.

### Run the website locally

Python 3.10 or later is recommended.

1. Clone or download this repository.
2. Open a terminal in the project folder.
3. Create and activate a virtual environment.

**Windows PowerShell**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

4. Install the dependencies.

```powershell
python -m pip install -r requirements.txt
```

5. Start the Streamlit app.

```powershell
streamlit run app.py
```

The website should open in your browser at the local URL printed in the terminal, usually `http://localhost:8501`.

## Deploy with Streamlit Community Cloud

1. Push the website files to a GitHub repository.
2. Make sure `app.py` and `requirements.txt` are in the repository.
3. Open [Streamlit Community Cloud](https://share.streamlit.io/).
4. Connect your GitHub account, choose the repository and branch, and select `app.py` as the app file.
5. Deploy the app and test the public URL.

### Installer hosting note

If `app.py` uses `st.download_button` to read `QuickConvert-Setup.exe` from the repository, the installer must be present in the deployed app's files. GitHub blocks individual files larger than 100 MB, and large downloads can consume the Streamlit app's memory. For a large installer or wider distribution, host the installer separately and link to its direct download URL instead.

## Important notes

- This repository's Streamlit website is a landing page and installer-distribution page; it does not itself perform file conversions in the browser.
- Test the installed Windows application on a separate computer before publicly distributing it.
- Verify every conversion and context-menu action in the release build before describing it as supported.
- Keep API keys, passwords, tokens, and private configuration out of GitHub. Store secrets in environment variables or Streamlit's secrets configuration.
- Update the version number, feature list, and support/contact details to match the actual release.

## License

No license is specified in this repository yet. Add a `LICENSE` file before publishing if you intend to grant others permission to use, modify, or redistribute the code. The installer and application may have separate licensing terms.
