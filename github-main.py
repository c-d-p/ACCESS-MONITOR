from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from datetime import datetime
from discord.ext import commands
import discord
from discord.utils import get

# Culture Kings AU
# Footlocker AU
#Kith
#Yeezy supply au
#laced au
#adidas au
#nike au
#jd sports au
#secret sneaker store

month = datetime.date(datetime.now()).strftime("%b")
day = datetime.date(datetime.now()).strftime("%d")

chrome_options = Options()
chrome_options.headless = True
chrome_options.add_argument('--disable-gpu')
TOKEN = "NzYwNjY5MDYzNTc1MzcxNzg2.X3PaRQ.-7fPTF1hWPM6gJZFDSOHsKhcAL0"
DRIVER_PATH = "C:\\Program Files (x86)\\chromedriver.exe"

### DISCORD ###
bot = commands.Bot(command_prefix='!')

#CHANNEL IDS
CKAU_ID = 760670703283339265

@bot.event
async def on_ready():
	print(f'{bot.user.name} has connected to Discord!')

def get_CKAU():
	driver = webdriver.Chrome(DRIVER_PATH, options=chrome_options)
	driver.get("https://www.culturekings.com.au/pages/all-releases#dropped")
	#time.sleep(5)
	#close_btn = driver.find_elements_by_xpath("//button[@type='button' and @aria-label='close']")[0]
	#close_btn.click()
	time.sleep(2)
	month_elements = driver.find_elements_by_xpath("//*[text()=" + day + "]")

	links = []
	for month_element in month_elements:
		parent = month_element.find_element_by_xpath("..")
		parent = parent.find_element_by_xpath("..")
		buybtn = parent.find_elements_by_tag_name("a")[1]
		buybtn_link = buybtn.get_attribute("href")
		links.append(buybtn_link)
	driver.quit()
	return links

@bot.command(name='CKAU')
async def send_CKAU(ctx):
	await ctx.message.add_reaction("\U0001F44D")
	links = get_CKAU()
	print(links)
	await ctx.send("New items from Culture Kings AU:")
	ck_ch = bot.get_channel(CKAU_ID)
	for link in links:
		await ck_ch.send(link)

bot.run(<"TOKEN GOES HERE">)