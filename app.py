import os
from pathlib import Path
import streamlit as st

st.set_page_config(
    page_title="QuickConvert | Files, simplified",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Put QuickConvert-Setup.exe in the same folder as app.py before deploying.
INSTALLER_PATH = Path(__file__).parent / "QuickConvert-Setup.exe"
APP_VERSION = "1.0.0"

st.markdown(
    r"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@400;500;600;700;800&display=swap');
    :root{--ink:#17231f;--muted:#68766f;--green:#baf36a;--cream:#f6f7f1;--line:rgba(23,35,31,.10)}
    .stApp{background:radial-gradient(circle at 84% 4%,rgba(186,243,106,.18),transparent 22rem),radial-gradient(circle at 8% 35%,rgba(194,220,203,.22),transparent 26rem),var(--cream);color:var(--ink);font-family:'DM Sans',sans-serif}
    [data-testid="stHeader"]{background:transparent}.block-container{max-width:1200px;padding-top:1.2rem;padding-bottom:4rem}#MainMenu,footer{visibility:hidden}
    .brand-row{display:flex;align-items:center;justify-content:space-between;padding:10px 0 24px;border-bottom:1px solid var(--line)}
    .brand{display:flex;align-items:center;gap:11px;font-family:Manrope,sans-serif;font-weight:800;font-size:1.12rem;letter-spacing:-.04em}
    .brand-mark{display:grid;place-items:center;width:38px;height:38px;border-radius:13px;color:#17231f;background:var(--green);box-shadow:0 7px 0 #8fc34e,0 12px 24px rgba(64,102,42,.15);transform:rotate(-5deg);font-size:1.25rem}
    .nav-pill{border:1px solid var(--line);padding:9px 15px;border-radius:99px;font-size:.83rem;color:#33463b;background:rgba(255,255,255,.55)}
    .hero{display:grid;grid-template-columns:1.04fr .96fr;gap:3rem;align-items:center;padding:64px 0 58px}
    .eyebrow{display:inline-flex;align-items:center;gap:8px;padding:8px 12px;border-radius:99px;background:#e8f5d9;color:#315a34;font-size:.78rem;font-weight:700;border:1px solid rgba(49,90,52,.08)}
    .eyebrow-dot{width:7px;height:7px;border-radius:50%;background:#69a943;box-shadow:0 0 0 4px rgba(105,169,67,.14)}
    h1.hero-title{font-family:Manrope,sans-serif;font-size:clamp(3rem,6.5vw,5.6rem);line-height:.99;letter-spacing:-.075em;font-weight:800;color:var(--ink);margin:22px 0}
    .hero-title span{color:#5e8c43}.hero-copy{color:var(--muted);font-size:1.12rem;line-height:1.8;max-width:520px;margin-bottom:25px}
    .visual-wrap{position:relative;min-height:430px;display:grid;place-items:center;perspective:1000px}
    .glow{position:absolute;width:330px;height:330px;border-radius:50%;background:rgba(186,243,106,.32);filter:blur(32px)}
    .orb{position:absolute;border-radius:50%;border:1px solid rgba(255,255,255,.75);box-shadow:inset -14px -20px 40px rgba(48,83,47,.12),0 25px 55px rgba(35,69,43,.13)}
    .orb.one{width:300px;height:300px;background:linear-gradient(145deg,#e9ffcb,#9fdf72 58%,#75b85c);transform:translate(20px,5px) rotateX(12deg) rotateY(-20deg)}
    .orb.two{width:205px;height:205px;background:linear-gradient(140deg,#fff,#d8e8d5 72%);transform:translate(-82px,45px) rotateY(24deg);opacity:.9}
    .orb.three{width:115px;height:115px;background:linear-gradient(145deg,#fdf8e9,#e9d9b4);transform:translate(108px,-100px) rotateX(30deg)}
    .float-card{position:absolute;z-index:3;padding:14px 16px;border-radius:18px;background:rgba(255,255,255,.86);border:1px solid rgba(255,255,255,.9);box-shadow:0 18px 45px rgba(30,55,37,.12);backdrop-filter:blur(14px);display:flex;align-items:center;gap:12px;animation:floaty 5s ease-in-out infinite}
    .float-card.a{top:70px;right:0;transform:rotate(4deg)}.float-card.b{bottom:60px;left:0;animation-delay:-2.1s}
    .file-icon{width:43px;height:48px;border-radius:11px;background:#edf6e6;display:grid;place-items:center;font-size:1.35rem}
    .float-label{font-size:.72rem;color:#78847c;margin-bottom:2px}.float-title{font-weight:800;font-size:.91rem;color:#24352b}
    .orbit{position:absolute;width:370px;height:240px;border:1px dashed rgba(65,111,64,.3);border-radius:50%;transform:rotate(-28deg)}
    @keyframes floaty{0%,100%{translate:0 0}50%{translate:0 -10px}}
    .section{padding:45px 0}.section-kicker{color:#5c8544;text-transform:uppercase;font-weight:800;letter-spacing:.14em;font-size:.72rem;margin-bottom:10px}
    .section-title{font-family:Manrope,sans-serif;font-size:clamp(2rem,4vw,3.2rem);font-weight:800;letter-spacing:-.06em;line-height:1.08;margin:0 0 14px}
    .section-copy{color:var(--muted);line-height:1.8;max-width:650px}
    .feature-card{height:100%;min-height:210px;padding:24px;border:1px solid rgba(29,55,39,.09);border-radius:24px;background:rgba(255,255,255,.72);box-shadow:0 8px 0 rgba(37,66,45,.035),0 18px 35px rgba(35,57,41,.045);transition:transform .25s ease,box-shadow .25s ease;transform-style:preserve-3d}
    .feature-card:hover{transform:translateY(-7px) rotateX(2deg) rotateY(-2deg);box-shadow:0 12px 0 rgba(37,66,45,.035),0 26px 45px rgba(35,57,41,.1)}
    .feature-icon{width:48px;height:48px;border-radius:16px;background:#edf7e3;display:grid;place-items:center;font-size:1.4rem;margin-bottom:19px;box-shadow:inset 0 1px 0 white}
    .feature-title{font-family:Manrope,sans-serif;font-weight:800;font-size:1.05rem;margin-bottom:8px}.feature-copy{color:var(--muted);font-size:.9rem;line-height:1.7}
    .steps{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-top:25px}.step{padding:20px;border-radius:20px;background:#203a2b;color:#f4f8ee;min-height:150px;box-shadow:0 7px 0 #15291e}
    .step-no{color:#baf36a;font-size:.76rem;font-weight:800;letter-spacing:.12em;margin-bottom:16px}.step-title{font-weight:800;font-size:1rem;margin-bottom:7px}.step-copy{font-size:.84rem;line-height:1.65;color:#c5d4c7}
    .download-panel{background:linear-gradient(135deg,#c9f58b,#a8e76b 55%,#8fd15b);border-radius:30px;padding:38px;position:relative;overflow:hidden;box-shadow:0 9px 0 #78b74d,0 24px 55px rgba(70,117,49,.16)}
    .download-panel:after{content:"";position:absolute;width:260px;height:260px;border-radius:50%;border:1px solid rgba(33,75,53,.15);right:-60px;top:-100px;box-shadow:0 0 0 24px rgba(33,75,53,.035),0 0 0 48px rgba(33,75,53,.025)}
    .download-title{font-family:Manrope,sans-serif;font-weight:800;letter-spacing:-.06em;font-size:clamp(2rem,4vw,3.25rem);line-height:1.08;max-width:680px;color:#1b3324;margin:0 0 12px}
    .download-copy{color:#36543a;line-height:1.8;max-width:600px;margin-bottom:22px}.small-note{font-size:.77rem;color:#526f4f;line-height:1.6;margin-top:12px}
    .footer{border-top:1px solid var(--line);margin-top:45px;padding-top:25px;color:#78847c;font-size:.8rem;display:flex;justify-content:space-between;gap:1rem;flex-wrap:wrap}
    div.stDownloadButton > button {
    border-radius: 999px !important;
    border: 1px solid #b7d99b !important;
    background: #e4f5d5 !important;
    color: #203a2b !important;
    padding: .85rem 1.25rem !important;
    font-weight: 800 !important;
    box-shadow: 0 5px 0 #c2dfa9 !important;
    transition: all .2s ease !important;
}

div.stDownloadButton > button:hover {
    background: #d3edbd !important;
    color: #172b20 !important;
    box-shadow: 0 7px 0 #b0d493 !important;
    transform: translateY(-2px);
}
    @media(max-width:850px){.hero{grid-template-columns:1fr;gap:1rem;padding:42px 0}.visual-wrap{min-height:350px}.orb.one{width:240px;height:240px}.orb.two{width:160px;height:160px}.orb.three{width:90px;height:90px}.float-card.a{right:2px;top:25px}.float-card.b{left:0;bottom:25px}.steps{grid-template-columns:1fr}.download-panel{padding:26px}}
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown("""
<div class="brand-row"><div class="brand"><div class="brand-mark">↗</div><span>QuickConvert</span></div><div class="nav-pill">Less file fuss. More flow. ✦</div></div>
<section class="hero"><div><div class="eyebrow"><span class="eyebrow-dot"></span> YOUR EVERYDAY FILE SIDEKICK</div>
<h1 class="hero-title">Files should<br>just <span>work.</span></h1>
<p class="hero-copy">Meet the calmer way to convert your files. QuickConvert keeps everyday file tasks simple, so you can spend less time hunting for tools and more time getting things done.</p></div>
<div class="visual-wrap"><div class="glow"></div><div class="orbit"></div><div class="orb one"></div><div class="orb two"></div><div class="orb three"></div>
<div class="float-card a"><div class="file-icon">📄</div><div><div class="float-label">READY WHEN YOU ARE</div><div class="float-title">PDF · DOCX · TXT</div></div></div>
<div class="float-card b"><div class="file-icon">✨</div><div><div class="float-label">A LITTLE LESS CLICKING</div><div class="float-title">Right-click to get started</div></div></div></div></section>
<div class="section-kicker">MADE FOR REAL LIFE</div><h2 class="section-title">Small tasks. Smoother days.</h2><p class="section-copy">A simple desktop companion for those “I just need to convert this file” moments. No complicated workflow, no cluttered dashboard—just a more comfortable way to get it done.</p>
""", unsafe_allow_html=True)

cols = st.columns(3, gap="medium")
features = [
    ("⚡", "A quicker workflow", "Start from the app or use the Windows right-click menu to bring a file into QuickConvert."),
    ("🧩", "Everyday formats", "Work with supported image, PDF, text, HTML, and Word document conversion workflows."),
    ("🫶", "Made to feel simple", "A friendly interface designed to keep the task clear and the experience approachable."),
]
for col, (icon, title, copy) in zip(cols, features):
    with col:
        st.markdown(f'<div class="feature-card"><div class="feature-icon">{icon}</div><div class="feature-title">{title}</div><div class="feature-copy">{copy}</div></div>', unsafe_allow_html=True)

st.markdown("""
<div class="section"><div class="section-kicker">THREE LITTLE STEPS</div><h2 class="section-title">From “ugh, this file”<br>to “all done.”</h2><p class="section-copy">QuickConvert is designed to keep the process straightforward.</p>
<div class="steps"><div class="step"><div class="step-no">01 / OPEN</div><div class="step-title">Choose your file</div><div class="step-copy">Open QuickConvert or start from a supported file in Windows Explorer.</div></div>
<div class="step"><div class="step-no">02 / CONVERT</div><div class="step-title">Pick your format</div><div class="step-copy">Choose a conversion supported by the app and follow the on-screen steps.</div></div>
<div class="step"><div class="step-no">03 / DONE</div><div class="step-title">Get back to life</div><div class="step-copy">Save your converted file and get on with what you were doing.</div></div></div></div>
<div class="section"><div class="download-panel"><div class="section-kicker">YOUR FILE SIDEKICK IS READY</div><h2 class="download-title">Make file conversion<br>one less thing to think about.</h2><p class="download-copy">Download QuickConvert for Windows and give your everyday file tasks a simpler home.</p></div></div>
""", unsafe_allow_html=True)

if INSTALLER_PATH.is_file():
    try:
        installer_size_mb = INSTALLER_PATH.stat().st_size / (1024 * 1024)
        if installer_size_mb > 150:
            st.warning(
                f"The installer is {installer_size_mb:.1f} MB. Streamlit's download button loads the file into app memory; "
                "for a large audience or large installer, a dedicated file host is more reliable."
            )
        with INSTALLER_PATH.open("rb") as installer_file:
            installer_bytes = installer_file.read()
        st.download_button(
            label="⬇  Download QuickConvert for Windows",
            data=installer_bytes,
            file_name="QuickConvert-Setup.exe",
            mime="application/octet-stream",
            use_container_width=True,
            help="Downloads the Windows installer.",
        )
        st.caption(f"QuickConvert for Windows · Version {APP_VERSION} · {installer_size_mb:.1f} MB")
    except OSError:
        st.error("The installer could not be read. Check that QuickConvert-Setup.exe is present and accessible.")
else:
    st.info(
        "To enable the download button, place `QuickConvert-Setup.exe` in the same folder as `app.py` "
        "before deploying the website."
    )

st.markdown('<p class="small-note">Windows desktop app. Some document conversions may depend on software installed on your computer.</p>', unsafe_allow_html=True)

st.markdown('<div class="section"><div class="section-kicker">A FEW QUICK ANSWERS</div><h2 class="section-title">Good to know.</h2></div>', unsafe_allow_html=True)
with st.expander("Is QuickConvert free?"):
    st.write("Add your confirmed pricing and license details here before publishing.")
with st.expander("Which file formats are supported?"):
    st.write("QuickConvert supports selected image, PDF, text, HTML, and Word document conversions. List only the conversions you have tested in your release build.")
with st.expander("Does it work from the Windows right-click menu?"):
    st.write("When installed and registered for supported file types, QuickConvert can be launched from Windows File Explorer.")
with st.expander("Are files uploaded to a website?"):
    st.write("This page only distributes the Windows installer. Describe the app's actual file-handling behavior accurately; only promise local processing if verified.")

st.markdown('<div class="footer"><div><strong style="color:#34483a">QuickConvert</strong> · A little more ease in your day.</div><div>Made for Windows · © 2026 QuickConvert</div></div>', unsafe_allow_html=True)
