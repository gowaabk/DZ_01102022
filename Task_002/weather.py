from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps



owm = OWM('c56797139654af6b6ba50259d1a0e9d3')
mgr = owm.weather_manager()


def find_weather(city):
    observation = mgr.weather_at_place(city)
    w = observation.weather

    """ w.detailed_status         # 'clouds'
        w.wind()                  # {'speed': 4.6, 'deg': 330}
        w.humidity                # 87
        w.temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
        w.rain                    # {}
        w.heat_index              # None
        w.clouds                  # 75
    """
    answer_test = w.temperature('celsius')
    my_temp = answer_test['temp']
    my_temp_max = answer_test['temp_max']
    my_temp_min = answer_test['temp_min']
    return (f'В городе {city}\nТемпература  равна {my_temp}\nМаксимальная температура равна {my_temp_max}\nМинимальная температура равнв {my_temp_min}')


