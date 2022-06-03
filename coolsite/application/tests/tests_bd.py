from django.test import TestCase
from application.models import Car

class MyTestClass(TestCase):
    def setUp(self) -> None:
        # Дабовляем данные в таблицу "Car"
        Car.objects.create(Name='Caldina', Colour='Белая', Odo=321000)

    def test_a(self):
        #Проверяем что запись создана
        a = Car.objects.get(Name='Caldina')
        self.assertEqual(a.Name, 'Caldina')
