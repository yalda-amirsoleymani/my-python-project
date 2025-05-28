import os

# Create the folder if it doesn't exist
os.makedirs("site", exist_ok=True)

with open("site/index.html", "w") as f:
    f.write(
        """
    <html>
      <head><title>CI/CD Project</title></head>
      <body>
        <h1>Hello from GitHub Actions!</h1>
        <p>This page was generated and deployed automatically.</p>
      </body>
    </html>
    """
    )
