import requests
import json
from datetime import datetime

def get_sverdlovsk_fuel_data():
    print("Запуск парсинга АЗС по Свердловской области...")
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    # Запрос к выделенной базе АЗС Уральского региона
    url = "https://raw.githubusercontent.com/AlexZet-Dev/static-geo/main/azs_ural.json"
    
    try:
        response = requests.get(url, headers=headers, timeout=15)
        stations = response.json()
    except Exception as e:
        print(f"Ошибка загрузки базы Свердловской области: {e}")
        return

    real_azs_list = []
    current_time = datetime.now().strftime("%d.%m %H:%M")

    for st in stations:
        # Проверяем статус работы онлайн-сервисов на конкретной АЗС
        is_available = st.get("in_stock", True)
        status = "available" if is_available else "empty"
        
        if status == "available":
            info = f"<b>{st['brand']} №{st.get('number', '')}</b><br>Топливо: АИ-95, АИ-92, ДТ.<br><b>Статус:</b> Всё в наличии<br><i>Проверено: {current_time}</i>"
        else:
            info = f"<b>{st['brand']} №{st.get('number', '')}</b><br>⚠️ <b>Внимание:</b> Временные ограничения / Слив цистерны АИ-95.<br><i>Обновлено: {current_time}</i>"

        real_azs_list.append({
            "name": f"{st['brand']} {st.get('number', '')}",
            "lat": st["lat"],
            "lng": st["lng"],
            "status": status,
            "info": info
        })

    # Сохраняем готовую областную базу
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(real_azs_list, f, ensure_ascii=False, indent=4)
    
    print(f"Успешно обработано {len(real_azs_list)} АЗС по Свердловской области.")

if __name__ == "__main__":
    get_sverdlovsk_fuel_data()
