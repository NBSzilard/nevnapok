from selenium import webdriver
from bs4 import BeautifulSoup
import time
from discord_webhook import DiscordWebhook

nevnapok = ["Példa1", "Példa2"]

webhookurl = "WEBHOOK_URL"

driver = webdriver.Chrome()

driver.get("https://mai-nevnap.hu/")

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

nevnap = soup.find("h2").get_text(strip=True)
print(f"A mai névnap: {nevnap}")

if nevnap in nevnapok:
    webhook = DiscordWebhook(url=webhookurl, content=f"Ma van **{nevnap}** névnapja!")
    response = webhook.execute()

time.sleep(2)

driver.close()

driver = webdriver.Chrome()

driver.get("https://mai-nevnap.hu/milyen-n%C3%A9vnap-lesz-holnap")

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

nevnap = soup.find("h2").get_text(strip=True)
print(f"A holnapi névnap: {nevnap}")

if nevnap in nevnapok:
    webhook = DiscordWebhook(url=webhookurl, content=f"Holnap lesz **{nevnap}** névnapja!")
    response = webhook.execute()

time.sleep(2)

driver.close()
