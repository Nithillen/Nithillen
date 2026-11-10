#!/usr/bin/env python3
"""
Generates modern, editorial SVG cards for Nithillen Jayaseelan's GitHub profile.
Inspired by Avi Vashishta's card-based aesthetic, tailored to quantitative finance,
biomedical ML research, and systems engineering.
"""

import os
from html import escape

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "cards")
os.makedirs(OUT, exist_ok=True)

# ----------------- Design Tokens -----------------
W = 880  # Full width for GitHub profile container
COL = W / 3  # 293.333px per column in a 3-column row
GAP = 12
TILE_W = COL - 8  # 285.333px actual card width

# Palette: Dark luxury titanium & obsidian with precision accent lighting
BG_DARK = "#090d16"
BG_CARD = "#0f1626"
BORDER = "#1e293b"
BORDER_HIGHLIGHT = "#334155"

TEXT_PRIMARY = "#f8fafc"
TEXT_SECONDARY = "#94a8b8"
TEXT_MUTED = "#64748b"

ACCENT_CYAN = "#38bdf8"
ACCENT_BLUE = "#3b82f6"
ACCENT_ROSE = "#f43f5e"
ACCENT_EMERALD = "#10b981"
ACCENT_AMBER = "#f59e0b"

SERIF = "Georgia, 'Times New Roman', serif"
SANS = "system-ui, -apple-system, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
MONO = "'SF Mono', Monaco, Consolas, 'Liberation Mono', Menlo, monospace"

BASE_ANIMATIONS = """
@keyframes rise {
  from { opacity: 0; transform: translateY(14px); }
  to { opacity: 1; transform: none; }
}
@keyframes fade {
  from { opacity: 0; }
  to { opacity: 1; }
}
@keyframes pulse {
  0%, 100% { opacity: 1; transform: scale(1); }
  50% { opacity: 0.35; transform: scale(0.85); }
}
@keyframes shine {
  0% { transform: translateX(-600px); }
  40%, 100% { transform: translateX(900px); }
}
@keyframes sheen {
  0% { transform: translateX(-300px) skewX(-20deg); }
  25%, 100% { transform: translateX(500px) skewX(-20deg); }
}
@keyframes nudge {
  0%, 100% { transform: none; }
  50% { transform: translate(3px, -3px); }
}
.r { opacity: 0; animation: rise 0.8s cubic-bezier(0.16, 1, 0.3, 1) both; transform-box: fill-box; }
.f { opacity: 0; animation: fade 0.9s ease-out both; }
.live { animation: pulse 2s ease-in-out infinite; transform-box: fill-box; transform-origin: center; }
.nu { transform-box: fill-box; animation: nudge 2s ease-in-out infinite; }
.sh { animation: sheen 6s ease-in-out infinite; }
@media (prefers-reduced-motion: reduce) {
  .r, .f, .live, .nu, .sh { animation: none !important; opacity: 1 !important; transform: none !important; }
}
"""

def wrap_text(text, limit=34):
    words = text.split()
    lines, current = [], []
    current_len = 0
    for w in words:
        if current_len + len(w) + 1 > limit:
            lines.append(" ".join(current))
            current = [w]
            current_len = len(w)
        else:
            current.append(w)
            current_len += len(w) + 1
    if current:
        lines.append(" ".join(current))
    return lines

def render_svg(w, h, body, label, extra_css="", left=0, right=0, bottom=12):
    total_w = w + left + right
    total_h = h + bottom
    content = f'<g transform="translate({left:.3f}, 0)">{body}</g>' if left else body
    css = BASE_ANIMATIONS + extra_css
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{total_w:.3f}" height="{total_h}" '
        f'viewBox="0 0 {total_w:.3f} {total_h}" role="img" aria-label="{escape(label)}">\n'
        f'<title>{escape(label)}</title>\n'
        f'<style>{css}</style>\n'
        f'{content}\n'
        f'</svg>'
    )

def write_card(filename, content):
    path = os.path.join(OUT, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Generated cards/{filename}")

# ==============================================================================
# 1. HERO BANNER
# ==============================================================================
def generate_hero():
    h = 390
    body = f"""
<defs>
  <linearGradient id="hero-bg" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0%" stop-color="#0a0f1d"/>
    <stop offset="50%" stop-color="#0e172a"/>
    <stop offset="100%" stop-color="#080c16"/>
  </linearGradient>
  <linearGradient id="hero-border" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.6"/>
    <stop offset="50%" stop-color="#1e293b" stop-opacity="0.8"/>
    <stop offset="100%" stop-color="#3b82f6" stop-opacity="0.4"/>
  </linearGradient>
  <linearGradient id="name-shimmer" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0%" stop-color="#ffffff"/>
    <stop offset="40%" stop-color="#ffffff"/>
    <stop offset="50%" stop-color="#38bdf8"/>
    <stop offset="60%" stop-color="#ffffff"/>
    <stop offset="100%" stop-color="#ffffff"/>
    <animateTransform attributeName="gradientTransform" type="translate"
      values="-700 0; 700 0; 700 0" keyTimes="0; 0.55; 1" dur="6.5s" begin="1.2s" repeatCount="indefinite"/>
  </linearGradient>
  <linearGradient id="grid-glow" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.08"/>
    <stop offset="100%" stop-color="#38bdf8" stop-opacity="0"/>
  </linearGradient>
  <clipPath id="hero-clip">
    <rect width="{W}" height="{h}" rx="14"/>
  </clipPath>
</defs>

<!-- Card Surface -->
<rect width="{W}" height="{h}" rx="14" fill="url(#hero-bg)"/>
<rect width="{W}" height="{h}" rx="14" fill="none" stroke="url(#hero-border)" stroke-width="1.2"/>

<!-- Decorative Tech Geometry -->
<g clip-path="url(#hero-clip)">
  <circle cx="{W - 80}" cy="100" r="220" fill="url(#grid-glow)"/>
  <circle cx="{W - 80}" cy="100" r="160" fill="none" stroke="#1e293b" stroke-width="1" stroke-dasharray="4,6" opacity="0.6"/>
  <circle cx="{W - 80}" cy="100" r="90" fill="none" stroke="#334155" stroke-width="1" stroke-dasharray="2,4" opacity="0.4"/>
  <!-- Minimalist Constellation Dots -->
  <circle cx="{W - 140}" cy="60" r="3" fill="#38bdf8" opacity="0.7"/>
  <circle cx="{W - 50}" cy="130" r="2.5" fill="#38bdf8" opacity="0.6"/>
  <circle cx="{W - 110}" cy="170" r="2" fill="#818cf8" opacity="0.5"/>
  <line x1="{W - 140}" y1="60" x2="{W - 50}" y2="130" stroke="#1e293b" stroke-width="1" opacity="0.4"/>
  <line x1="{W - 50}" y1="130" x2="{W - 110}" y2="170" stroke="#1e293b" stroke-width="1" opacity="0.4"/>
</g>

<!-- Live Status Pill -->
<g class="f" style="animation-delay: 0.1s">
  <rect x="42" y="38" width="8" height="8" rx="2" fill="{ACCENT_CYAN}" class="live"/>
  <text x="58" y="46" font-family="{MONO}" font-size="11.5" letter-spacing="1.4" fill="{TEXT_MUTED}">M.SC. DATA SCIENCE &amp; MACHINE LEARNING · NUS SINGAPORE</text>
</g>

<!-- Main Headline Name -->
<text class="r" style="animation-delay: 0.25s" x="40" y="142" font-family="{SERIF}" font-size="82" font-weight="700" letter-spacing="-1.5" fill="{TEXT_PRIMARY}">Nithillen</text>
<text class="r" style="animation-delay: 0.4s" x="40" y="224" font-family="{SERIF}" font-style="italic" font-size="82" letter-spacing="-1.5" fill="url(#name-shimmer)">Jayaseelan</text>

<!-- Subtitle / Bio -->
<g class="r" style="animation-delay: 0.6s">
  <text x="42" y="272" font-family="{SANS}" font-size="16" font-weight="400" fill="{TEXT_SECONDARY}">Quantitative Developer &amp; Machine Learning Researcher</text>
  <text x="42" y="298" font-family="{SANS}" font-size="14.5" font-weight="400" fill="{TEXT_MUTED}">Focusing on statistical arbitrage, evolutionary algorithms, and intelligent clinical AI systems.</text>
</g>

<!-- Footer Meta & Links -->
<g class="f" style="animation-delay: 0.85s">
  <line x1="42" y1="334" x2="{W - 42}" y2="334" stroke="{BORDER}" stroke-width="1"/>
  
  <text x="42" y="362" font-family="{MONO}" font-size="12" fill="{TEXT_MUTED}">SINGAPORE</text>
  <text x="142" y="362" font-family="{MONO}" font-size="12" fill="{BORDER_HIGHLIGHT}">·</text>
  <text x="162" y="362" font-family="{MONO}" font-size="12" fill="{TEXT_MUTED}">5G PATENT AUTHOR</text>
  <text x="312" y="362" font-family="{MONO}" font-size="12" fill="{BORDER_HIGHLIGHT}">·</text>
  <text x="332" y="362" font-family="{MONO}" font-size="12" fill="{TEXT_MUTED}">B.TECH ECE (8.8 CGPA)</text>

  <g transform="translate({W - 200}, 362)">
    <text x="0" y="0" font-family="{MONO}" font-size="12" fill="{TEXT_SECONDARY}">linkedin / github</text>
    <text class="nu" x="125" y="0" font-family="{MONO}" font-size="12" fill="{ACCENT_CYAN}">↗</text>
  </g>
</g>
"""
    content = render_svg(W, h, body, "Nithillen Jayaseelan - Quantitative Developer and Machine Learning Researcher at NUS")
    write_card("hero.svg", content)

# ==============================================================================
# 2. DOMAIN TILES (3-COLUMN ROW)
# ==============================================================================
def generate_tile(filename, pos, label, accent_color, bg_gradient_stops, stat_num, stat_word, blurb_lines):
    h = 210
    left_pad = 4 * pos
    right_pad = 8 - 4 * pos
    delay = 0.3 + pos * 0.15

    blurb_svg = "".join(
        f'<text class="r" style="animation-delay: {delay + 0.6 + i * 0.08:.2f}s" x="22" y="{148 + i * 20}" '
        f'font-family="{SANS}" font-size="13" fill="{TEXT_SECONDARY}">{escape(line)}</text>'
        for i, line in enumerate(blurb_lines)
    )

    body = f"""
<defs>
  <linearGradient id="bg-{pos}" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0%" stop-color="{bg_gradient_stops[0]}"/>
    <stop offset="100%" stop-color="{bg_gradient_stops[1]}"/>
  </linearGradient>
  <clipPath id="card-clip-{pos}">
    <rect width="{TILE_W:.3f}" height="{h}" rx="12"/>
  </clipPath>
  <linearGradient id="sheen-{pos}" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0%" stop-color="#ffffff" stop-opacity="0"/>
    <stop offset="50%" stop-color="#ffffff" stop-opacity="0.08"/>
    <stop offset="100%" stop-color="#ffffff" stop-opacity="0"/>
  </linearGradient>
</defs>

<!-- Card Surface -->
<g clip-path="url(#card-clip-{pos})">
  <rect width="{TILE_W:.3f}" height="{h}" rx="12" fill="url(#bg-{pos})"/>
  <rect width="{TILE_W:.3f}" height="{h}" rx="12" fill="none" stroke="{BORDER}" stroke-width="1"/>
  <!-- Ambient glow circle -->
  <circle cx="{TILE_W - 30}" cy="30" r="80" fill="{accent_color}" opacity="0.06"/>
  <!-- Animated Sheen -->
  <rect class="sh" style="animation-delay: {delay + 1.2:.2f}s" x="0" y="0" width="100" height="{h}" fill="url(#sheen-{pos})"/>
</g>

<!-- Category Label -->
<g class="r" style="animation-delay: {delay + 0.2:.2f}s">
  <rect x="22" y="24" width="6" height="6" rx="1.5" fill="{accent_color}"/>
  <text x="34" y="30" font-family="{MONO}" font-size="11" letter-spacing="1.2" fill="{accent_color}">{escape(label)}</text>
  <text class="nu" x="{TILE_W - 32}" y="30" font-family="{MONO}" font-size="12" fill="{TEXT_MUTED}">↗</text>
</g>

<!-- Primary Metric / Headline -->
<g class="r" style="animation-delay: {delay + 0.4:.2f}s">
  <text x="22" y="104" font-family="{SERIF}" font-size="44" font-weight="700" fill="{TEXT_PRIMARY}">{escape(stat_num)} <tspan font-style="italic" font-size="34" fill="{accent_color}">{escape(stat_word)}</tspan></text>
</g>

<!-- Description Blurb -->
{blurb_svg}
"""
    content = render_svg(TILE_W, h, body, f"{label}: {stat_num} {stat_word}", left=left_pad, right=right_pad)
    write_card(filename, content)

# ==============================================================================
# 3. SECTION TITLE
# ==============================================================================
def generate_section_title(filename, plain_text, italic_text):
    h = 56
    body = f"""
<g class="r" style="animation-delay: 0.2s">
  <text x="2" y="38" font-family="{SERIF}" font-size="32" font-weight="600" fill="{TEXT_PRIMARY}">{escape(plain_text)} <tspan font-style="italic" fill="{ACCENT_CYAN}">{escape(italic_text)}</tspan></text>
  <line x1="340" y1="30" x2="{W}" y2="30" stroke="{BORDER}" stroke-width="1" stroke-dasharray="2,6"/>
</g>
"""
    content = render_svg(W, h, body, f"{plain_text} {italic_text}", bottom=4)
    write_card(filename, content)

# ==============================================================================
# 4. REPOSITORY CARDS (3-COLUMN ROW)
# ==============================================================================
def generate_repo_card(filename, pos, repo_name, category_tag, accent_color, desc_lines, tech_stack):
    h = 200
    left_pad = 4 * pos
    right_pad = 8 - 4 * pos
    delay = 0.4 + pos * 0.12

    desc_svg = "".join(
        f'<text class="r" style="animation-delay: {delay + 0.4 + i * 0.08:.2f}s" x="20" y="{86 + i * 19}" '
        f'font-family="{SANS}" font-size="12.5" fill="{TEXT_SECONDARY}">{escape(line)}</text>'
        for i, line in enumerate(desc_lines)
    )

    body = f"""
<defs>
  <linearGradient id="repo-bg-{pos}" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0%" stop-color="#0c1220"/>
    <stop offset="100%" stop-color="#080c16"/>
  </linearGradient>
</defs>

<!-- Card Surface -->
<rect width="{TILE_W:.3f}" height="{h}" rx="12" fill="url(#repo-bg-{pos})"/>
<rect width="{TILE_W:.3f}" height="{h}" rx="12" fill="none" stroke="{BORDER}" stroke-width="1"/>

<!-- Header: Tag & Language -->
<g class="r" style="animation-delay: {delay + 0.1:.2f}s">
  <rect x="20" y="20" width="6" height="6" rx="1.5" fill="{accent_color}"/>
  <text x="32" y="26" font-family="{MONO}" font-size="10.5" letter-spacing="1" fill="{accent_color}">{escape(category_tag)}</text>
  <text class="nu" x="{TILE_W - 28}" y="26" font-family="{MONO}" font-size="11" fill="{TEXT_MUTED}">↗</text>
</g>

<!-- Repository Title -->
<g class="r" style="animation-delay: {delay + 0.25:.2f}s">
  <text x="20" y="58" font-family="{MONO}" font-size="15" font-weight="600" fill="{TEXT_PRIMARY}">{escape(repo_name)}</text>
</g>

<!-- Description Lines -->
{desc_svg}

<!-- Tech Stack Pill at Bottom -->
<g class="f" style="animation-delay: {delay + 0.7:.2f}s">
  <line x1="20" y1="{h - 38}" x2="{TILE_W - 20}" y2="{h - 38}" stroke="{BORDER}" stroke-width="1"/>
  <text x="20" y="{h - 18}" font-family="{MONO}" font-size="11" fill="{TEXT_MUTED}">{escape(tech_stack)}</text>
</g>
"""
    content = render_svg(TILE_W, h, body, f"{repo_name} - {category_tag}", left=left_pad, right=right_pad)
    write_card(filename, content)


if __name__ == "__main__":
    print("Generating profile cards...")

    # 1. Hero
    generate_hero()

    # 2. Three Metric / Domain Milestone Tiles
    generate_tile(
        "tile-quant.svg", 0, "QUANT & ALGORITHMS", ACCENT_CYAN,
        ("#0f172a", "#080d1a"),
        "3", "Engines",
        ["Autonomous evolutionary trading,", "XGBoost pairs arbitrage &", "append-only safe vaults."]
    )

    generate_tile(
        "tile-research.svg", 1, "PATENT & RESEARCH", ACCENT_ROSE,
        ("#1a0f1d", "#0d0812"),
        "0.98", "R² Score",
        ["5G bandwidth optimization patent", "(No. 202541116411) & published", "PPG biometric ML paper."]
    )

    generate_tile(
        "tile-systems.svg", 2, "ENTERPRISE AI & IOT", ACCENT_EMERALD,
        ("#081a16", "#040e0b"),
        "Production", "Scale",
        ["SyncAgent compliance workflows,", "LLM transcript automation &", "smart IoT telemetry systems."]
    )

    # 3. Section Title
    generate_section_title("title-systems.svg", "Featured Systems &", "Architectures")

    # 4. Three Repository Showcase Cards
    generate_repo_card(
        "repo-evolutionary.svg", 0,
        "evolutionary_trading", "ALGORITHMIC TRADING", ACCENT_CYAN,
        ["Autonomous agents spawn, mutate", "and trade. Profits locked into", "append-only vault via House Money."],
        "Python · asyncio · OOP"
    )

    generate_repo_card(
        "repo-readmission.svg", 1,
        "readmission_engine", "CLINICAL ML & SQL", ACCENT_EMERALD,
        ["MIMIC-III clinical wrangling via", "CTEs & LEAD(). Random Forest", "with SHAP stakeholder reporting."],
        "Python · SQL · Scikit-Learn · SHAP"
    )

    generate_repo_card(
        "repo-pairs.svg", 2,
        "pairs_trading_ml", "STATISTICAL ARBITRAGE", ACCENT_ROSE,
        ["Cointegration spread forecasting", "using XGBoost classifier with", "VectorBT backtesting engine."],
        "Python · XGBoost · Statsmodels"
    )

    print("All profile cards successfully rendered!")
