"""SmartBot 推广图生成器 - Free & Open Source"""
from PIL import Image, ImageDraw, ImageFont
import os

OUT = r"C:\Users\16846\.qclaw\workspace-agent-b1823e5f\projects\smartbot\promo_images"
os.makedirs(OUT, exist_ok=True)

C = {
    'indigo600': (99, 102, 241),
    'indigo700': (67, 56, 202),
    'indigo900': (30, 27, 75),
    'purple600': (147, 51, 234),
    'purple700': (126, 34, 206),
    'green500': (34, 197, 94),
    'green600': (22, 163, 74),
    'green100': (220, 252, 231),
    'slate900': (15, 23, 42),
    'slate800': (30, 41, 59),
    'slate700': (51, 65, 85),
    'slate600': (71, 85, 105),
    'slate500': (100, 116, 139),
    'slate400': (148, 163, 184),
    'white': (255, 255, 255),
    'black': (0, 0, 0),
    'cyan500': (6, 182, 212),
    'orange500': (245, 158, 11),
    'pink500': (236, 72, 153),
    'blue600': (37, 99, 235),
}

def font(size):
    for p in [r"C:\Windows\Fonts\arial.ttf", r"C:\Windows\Fonts\segoeui.ttf"]:
        try: return ImageFont.truetype(p, size)
        except: pass
    return ImageFont.load_default()

def grad(w, h, c1, c2):
    img = Image.new("RGB", (w, h))
    d = ImageDraw.Draw(img)
    for y in range(h):
        r = int(c1[0]*(1-y/h) + c2[0]*y/h)
        g = int(c1[1]*(1-y/h) + c2[1]*y/h)
        b = int(c1[2]*(1-y/h) + c2[2]*y/h)
        d.line([(0,y),(w,y)], fill=(r,g,b))
    return img, d

def rr(img, d, x1, y1, x2, y2, r, fill):
    h = y2 - y1; w = x2 - x1; r = min(r, h//2, w//2)
    if r <= 0: d.rectangle([x1,y1,x2,y2], fill=fill); return
    d.pieslice([x1,y1,x1+2*r,y1+2*r], 180, 270, fill=fill)
    d.pieslice([x2-2*r,y1,x2,y1+2*r], 270, 360, fill=fill)
    d.pieslice([x1,y2-2*r,x1+2*r,y2], 90, 180, fill=fill)
    d.pieslice([x2-2*r,y2-2*r,x2,y2], 0, 90, fill=fill)
    d.rectangle([x1+r,y1,x2-r,y2], fill=fill)
    d.rectangle([x1,y1+r,x2,y2-r], fill=fill)

def txt_c(d, text, cx, y, size, color):
    f = font(size); bb = d.textbbox((0,0), text, font=f); w = bb[2]-bb[0]
    d.text((cx-w//2, y), text, font=f, fill=color)

def txt_l(d, text, x, y, size, color):
    f = font(size); d.text((x, y), text, font=f, fill=color)


# ==================== 图1: Hero Banner ====================
def fig1():
    W, H = 1200, 630
    img, d = grad(W, H, C['indigo900'], C['slate900'])
    d.ellipse([700,-100,1200,400], fill=(99,102,241,30))
    d.ellipse([-50,400,450,900], fill=(147,51,234,30))

    # Logo
    rr(img, d, 80, 50, 135, 105, 12, C['indigo600'])
    txt_l(d, "S", 93, 55, 32, C['white'])
    txt_l(d, "SmartBot", 148, 62, 28, C['white'])
    rr(img, d, 285, 56, 440, 88, 18, (22,163,74,60))
    txt_l(d, "FREE & OPEN SOURCE", 295, 63, 14, C['green500'])

    # 免费标签
    rr(img, d, 470, 56, 580, 88, 18, C['green500'])
    txt_l(d, "MIT LICENSE", 488, 63, 14, C['white'])

    # 标题
    txt_c(d, "AI Customer Service", 600, 175, 52, C['white'])
    txt_c(d, "100% Free & Open Source", 600, 240, 54, C['green500'])
    txt_c(d, "Deploy in 5 min  |  No vendor lock-in  |  MIT License", 600, 320, 22, C['slate400'])

    # 按钮
    rr(img, d, 340, 370, 560, 420, 14, C['green500'])
    txt_c(d, "View on GitHub", 450, 378, 22, C['white'])
    rr(img, d, 600, 370, 820, 420, 14, C['slate800'])
    txt_c(d, "Try Demo", 710, 378, 22, C['white'])

    # 底部
    txt_l(d, "github.com/PHclaw/smartbot", 80, 580, 16, C['slate500'])
    txt_l(d, "MIT License", 800, 560, 28, C['green500'])
    txt_l(d, "No Subscription", 800, 592, 14, C['slate500'])
    txt_l(d, "Deploy Anywhere", 950, 560, 28, C['cyan500'])
    txt_l(d, "Self-Host", 950, 592, 14, C['slate500'])
    txt_l(d, "Open Source", 1100, 560, 28, C['purple600'])
    txt_l(d, "Fork & Customize", 1100, 592, 14, C['slate500'])

    img.save(f"{OUT}/01_hero_banner.png")
    print("[OK] 01_hero_banner.png")


# ==================== 图2: 功能展示 ====================
def fig2():
    W, H = 1200, 630
    img, d = grad(W, H, C['slate900'], C['slate900'])

    txt_c(d, "Everything You Need", 600, 50, 42, C['white'])
    txt_c(d, "A complete AI customer service solution - 100% free and open source", 600, 100, 20, C['slate400'])

    feats = [
        ("5-Min Setup", "Drag-and-drop config.\nNo engineers needed.", C['indigo600']),
        ("AI-Powered", "RAG knowledge base.\nUnderstands intent.", C['purple600']),
        ("Multi-Channel", "Web / WhatsApp / WeChat\n/ Xiaohongshu", C['cyan500']),
        ("Human Handoff", "Seamless transfer to\nhuman agents.", C['green500']),
        ("Analytics", "Conversation analysis,\nintent tracking.", C['orange500']),
        ("100% Free", "MIT License. Deploy\nanywhere. Forever.", C['green500']),
    ]

    cw, ch = 360, 200; gap = 28
    sx = (W - 3*cw - 2*gap)//2; sy = 165

    for i, (title, desc, color) in enumerate(feats):
        col = i%3; row = i//3
        x = sx + col*(cw+gap); y = sy + row*(ch+gap)
        rr(img, d, x, y, x+cw, y+ch, 14, C['slate800'])
        rr(img, d, x+14, y+14, x+cw-14, y+54, 8, color)
        txt_c(d, title, x+cw//2, y+26, 18, C['white'])
        for j, line in enumerate(desc.split('\n')):
            txt_l(d, line, x+20, y+74+j*25, 15, C['slate400'])

    img.save(f"{OUT}/02_features.png")
    print("[OK] 02_features.png")


# ==================== 图3: 开源 + MIT ====================
def fig3():
    W, H = 1200, 630
    img, d = grad(W, H, C['green500'], C['indigo600'])

    # 装饰
    d.ellipse([-100, -100, 500, 500], fill=(255,255,255,20))
    d.ellipse([700, 200, 1300, 800], fill=(255,255,255,15))

    txt_c(d, "100% FREE & OPEN SOURCE", 600, 80, 38, C['white'])
    txt_c(d, "No Subscription", 600, 170, 80, C['white'])
    txt_c(d, "No Per-Message Fees", 600, 270, 60, C['white'])
    txt_c(d, "MIT License - Deploy Anywhere", 600, 360, 28, C['green100'])

    # 三个特点
    items = [
        ("No Lock-in", "Deploy on your\nown servers"),
        ("Community", "Open to\ncontributions"),
        ("Forever Free", "No vendor\ncommitment"),
    ]
    tw, th = 300, 120; gap = 50
    sx = (W - 3*tw - 2*gap)//2; sy = 440
    for i, (title, desc) in enumerate(items):
        x = sx + i*(tw+gap)
        rr(img, d, x, sy, x+tw, sy+th, 16, (255,255,255,25))
        txt_c(d, title, x+tw//2, sy+15, 24, C['white'])
        for j, line in enumerate(desc.split('\n')):
            txt_c(d, line, x+tw//2, sy+50+j*28, 16, (220,252,231))

    txt_c(d, "github.com/PHclaw/smartbot", 600, 600, 20, C['white'])
    img.save(f"{OUT}/03_free.png")
    print("[OK] 03_free.png")


# ==================== 图4: Demo ====================
def fig4():
    W, H = 900, 600
    img = Image.new("RGB", (W, H), C['slate900'])
    d = ImageDraw.Draw(img)

    d.rectangle([0,0,W,50], fill=C['slate800'])
    d.ellipse([20,15,35,30], fill=(239,68,68))
    d.ellipse([50,15,65,30], fill=(245,158,11))
    d.ellipse([80,15,95,30], fill=(34,197,94))
    txt_c(d, "Try SmartBot - Free AI Customer Service", 450, 16, 15, C['slate400'])

    cx, cy = 150, 80; cw, ch = 600, 440
    rr(img, d, cx, cy, cx+cw, cy+ch, 15, C['slate800'])
    d.rectangle([cx, cy, cx+cw, cy+60], fill=C['slate700'])
    rr(img, d, cx+15, cy+12, cx+48, cy+48, 18, C['green500'])
    txt_l(d, "S", cx+25, cy+16, 18, C['white'])
    txt_l(d, "SmartBot", cx+58, cy+15, 18, C['white'])
    txt_l(d, "Free & Open", cx+58, cy+35, 13, C['green500'])
    d.rectangle([cx+10, cy+70, cx+cw-10, cy+ch-70], fill=(26,32,44))

    msgs = [
        ("ai", "Hi! SmartBot is 100% free.\nAsk me anything!"),
        ("user", "Is it really free?"),
        ("ai", "Yes! 100% free and open source.\nMIT License - deploy anywhere.\nNo subscription, no fees."),
        ("user", "What features?"),
        ("ai", "SmartBot features:\n+ AI-powered replies\n+ Multi-channel\n+ Human handoff\n+ Analytics\n\nAll free forever."),
    ]

    my = cy + 85
    for role, text in msgs:
        if role == "ai":
            lines = text.split('\n')
            h = 20 + len(lines)*18
            rr(img, d, cx+20, my, cx+360, my+h, 10, C['slate700'])
            for j, line in enumerate(lines):
                txt_l(d, line, cx+30, my+8+j*18, 14, C['white'])
            my += h + 15
        else:
            rr(img, d, cx+cw-360, my, cx+cw-20, my+40, 10, C['green500'])
            txt_l(d, text, cx+cw-350, my+10, 14, C['white'])
            my += 55

    iy = cy + ch - 55
    rr(img, d, cx+10, iy, cx+cw-90, iy+40, 10, C['slate700'])
    txt_l(d, "Try it free...", cx+20, iy+10, 16, C['slate500'])
    rr(img, d, cx+cw-80, iy, cx+cw-20, iy+40, 10, C['green500'])
    txt_c(d, "Send", cx+cw-50, iy+9, 16, C['white'])

    img.save(f"{OUT}/04_demo.png")
    print("[OK] 04_demo.png")


# ==================== 图5: AgentFlow ====================
def fig5():
    W, H = 1200, 630
    img, d = grad(W, H, (10,15,50), C['indigo900'])
    d.ellipse([700,-150,1200,350], fill=(30,64,175,40))
    d.ellipse([-100,350,500,900], fill=(76,29,149,40))

    rr(img, d, 80, 50, 135, 105, 12, C['blue600'])
    txt_l(d, "A", 93, 55, 32, C['white'])
    txt_l(d, "AgentFlow", 148, 62, 28, C['white'])
    rr(img, d, 310, 56, 430, 88, 18, (37,99,235,80))
    txt_l(d, "AI Agent Platform", 322, 63, 14, (140,170,255))

    txt_c(d, "Build AI Agents", 600, 195, 50, C['white'])
    txt_c(d, "100% Free & Open Source", 600, 258, 52, C['blue600'])
    txt_c(d, "No-code builder  |  Ready-made templates", 600, 345, 22, C['slate400'])

    rr(img, d, 340, 395, 565, 450, 14, C['green500'])
    txt_c(d, "View on GitHub", 452, 403, 22, C['white'])
    rr(img, d, 610, 395, 830, 450, 14, C['slate800'])
    txt_c(d, "Star on GitHub", 720, 403, 22, C['white'])

    tags = ["Drag-and-Drop Builder", "Ready-made Templates", "RAG Knowledge Base", "Tool Calling"]
    tw, th = 175, 45; tg = 18; total = len(tags)*tw+(len(tags)-1)*tg
    sx = (W-total)//2
    for i, tag in enumerate(tags):
        x = sx + i*(tw+tg)
        rr(img, d, x, 520, x+tw, 565, 10, C['slate800'])
        txt_c(d, tag, x+tw//2, 533, 15, C['white'])

    txt_l(d, "github.com/PHclaw/agentflow", 80, 590, 16, C['slate500'])
    img.save(f"{OUT}/05_agentflow.png")
    print("[OK] 05_agentflow.png")


# ==================== 图6: 小红书 ====================
def fig6():
    W, H = 1242, 1660
    img, d = grad(W, H, C['indigo600'], C['purple700'])
    d.ellipse([(W-320)//2, 80, (W+320)//2, 400], fill=(255,255,255,25))
    d.ellipse([(W-220)//2, 160, (W+220)//2, 400], fill=(255,255,255,15))
    txt_c(d, "S", W//2, 220, 80, C['white'])

    txt_c(d, "SmartBot", W//2, 420, 96, C['white'])
    txt_c(d, "Free & Open Source AI Customer Service", W//2, 535, 42, C['white'])

    by = 700
    rr(img, d, 100, by, W-100, by+450, 50, (255,255,255,22))
    txt_c(d, "I Built an AI Customer Service", W//2, by+50, 48, C['white'])
    txt_c(d, "100% Free Forever", W//2, by+110, 36, C['green100'])

    lines = [
        "Setup in 5 minutes",
        "No subscription fees",
        "MIT License - deploy anywhere",
        "Perfect for small teams",
    ]
    for i, line in enumerate(lines):
        txt_c(d, "[ " + line + " ]", W//2, by+180+i*60, 34, C['white'])

    # 标签
    tags = ["100% FREE", "OPEN SOURCE", "MIT LICENSE"]
    total = len(tags)*160+(len(tags)-1)*20
    sx = (W-total)//2
    for i, tag in enumerate(tags):
        x = sx + i*180
        rr(img, d, x, 1280, x+160, 1320, 30, C['green500'])
        txt_c(d, tag, x+80, 1293, 20, C['white'])

    txt_c(d, "github.com/PHclaw/smartbot", W//2, 1420, 30, C['white'])
    img.save(f"{OUT}/06_xiaohongshu.png", quality=95)
    print("[OK] 06_xiaohongshu.png")


if __name__ == "__main__":
    print("[*] Generating...")
    fig1(); fig2(); fig3(); fig4(); fig5(); fig6()
    print(f"[*] Done: {OUT}")
