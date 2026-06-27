import json
import requests
import os
from datetime import datetime

def fetch_fuel_data():
    print("Начало сбора данных о бензине...")
    
    # ТУТ БУДЕТ ВАШ КОД ПАРСИНГА. 
    # В качестве демонстрации мы эмулируем получение данных с сервера АЗС:
    current_time = datetime.now().strftime("%H:%M:%S")
    
    # Пример структуры, которую отдают парсеры
    azs_dynamic_data = [
        {
            "name": "Газпромнефть №102",
            "lat": 56.845,
            "lng": 60.612,
            "status": "available",
            "info": f"АИ-95 и АИ-92 в наличии. Обновлено в {current_time}."
        },
        {
            "name": "Лукойл №24",
            "lat": 56.830,
            "lng": 60.580,
            "status": "empty",
            "info": f"Внимание! АИ-95 временно отсутствует. Данные на {current_time}."
        },
        {
            "name": "Роснефть на въезде",
            "lat": 56.860,
            "lng": 60.640,
            "status": "available",
            "info": f"Все виды топлива, включая ДТ. Проверенно в {current_time}."
        }
    ]
    
    # Сохраняем результат в файл, который прочитает наша карта
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(azs_dynamic_data, f, ensure_ascii=False, indent=4)
    
    print("Данные успешно сохранены в data.json")

if __name__ == "__main__":
    fetch_fuel_data()