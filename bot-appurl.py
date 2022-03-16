from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from webdriver_manager.chrome import ChromeDriverManager

chrome_manager = ChromeDriverManager()
driver = webdriver.Chrome(chrome_manager.install())

default_url = 'https://web.whatsapp.com/send?1=pt_BR&phone='

number_prefix = '5561'

message = 'Teste de Automatização. A expressão Lorem ipsum em design gráfico e editoração é um texto padrão em latim utilizado na produção gráfica para preencher os espaços de texto em publicações (jornais, revistas, e sites) para testar e ajustar aspectos visuais (layout, tipografia, formatação, etc.) antes de utilizar conteúdo real. Também é utilizado em catálogos tipográficos, para demonstrar textos e títulos escritos com as fontes.[1]'

phone_numbers = [
  '987654321'
]

is_first_time_open_page = True

def open_contact_url(phone_number: str):
  complete_url = default_url + number_prefix + phone_number
  driver.get(complete_url)

  if is_first_time_open_page:
    time.sleep(20)
  else:
    time.sleep(7)

def send_message(message: str):
  message_field_element = driver.find_elements_by_xpath('//div[contains(@class, "copyable-text selectable-text")]')[1]
  message_field_element.click()
  message_field_element.send_keys(message)
  message_field_element.send_keys(Keys.ENTER)

  global is_first_time_open_page

  if is_first_time_open_page:
    is_first_time_open_page = False

  time.sleep(1.5)

for phone_number in phone_numbers:
  open_contact_url(phone_number)
  send_message(message)