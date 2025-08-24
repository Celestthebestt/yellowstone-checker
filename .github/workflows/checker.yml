name: Yellowstone Checker

on:
  schedule:
    - cron: "0 * * * *"   # Runs every hour
  workflow_dispatch:       # Lets you run manually

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repo
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.x"

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install requests beautifulsoup4

      - name: Run script
        env:
          EMAIL_ADDRESS: ${{ secrets.EMAIL_ADDRESS }}
          EMAIL_PASSWORD: ${{ secrets.EMAIL_PASSWORD }}
        run: python yellowstone_checker.py
