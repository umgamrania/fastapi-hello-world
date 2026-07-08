from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Hello World</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Pinyon+Script&family=Cormorant+Garamond:ital,wght@0,400;0,500;1,400&display=swap" rel="stylesheet">
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }

  body {
    height: 100vh;
    background: radial-gradient(circle at center, #0d0d0d 0%, #000000 100%);
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
  }

  .container {
    text-align: center;
  }

  h1 {
    font-family: 'Pinyon Script', cursive;
    font-size: 7rem;
    font-weight: 400;
    letter-spacing: 0.03em;
    background: linear-gradient(135deg, #f5e7c1 0%, #d4af37 45%, #fff6da 55%, #b8860b 100%);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
    text-shadow: 0 0 40px rgba(212, 175, 55, 0.25);
  }

  p.subtitle {
    margin-top: 1rem;
    font-family: 'Cormorant Garamond', serif;
    font-style: italic;
    font-weight: 400;
    font-size: 1.4rem;
    letter-spacing: 0.15em;
    color: #cfae5e;
    text-transform: uppercase;
  }

  .line {
    width: 120px;
    height: 1px;
    margin: 1.5rem auto;
    background: linear-gradient(90deg, transparent, #d4af37, transparent);
  }
</style>
</head>
<body>
  <div class="container">
    <h1>Heheheheh Changed!!!!!!</h1>
    <div class="line"></div>
    <p class="subtitle">Crafted with Elegance</p>
  </div>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return HTML_PAGE
