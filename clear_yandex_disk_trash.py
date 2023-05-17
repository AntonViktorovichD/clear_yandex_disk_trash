import requests
import logging
from datetime import datetime

TOKEN = '***********************'

# Настройка логирования
log_filename = '/home/grand/web/grand.gold/public_html/clear_yandex_disk_trash.log'
logging.basicConfig(filename=log_filename, level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def clear_trash():
    url = 'https://cloud-api.yandex.net/v1/disk/trash/resources'
    headers = {'Authorization': f'OAuth {TOKEN}'}
    params = {'path': '/'}

    response = requests.delete(url, headers=headers, params=params)

    if response.status_code == 204:
        logging.info('Trash has been cleared successfully.')
    elif response.status_code == 202:
        logging.info('Deletion is in progress.')
    else:
        logging.error(f'Error occurred: {response.status_code}')

if __name__ == '__main__':
    clear_trash()
