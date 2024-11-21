from .models import LegoToy

class LegoDataManager:
    @staticmethod
    def save_toys(toys):
        existing_toy_ids = []

        for toy in toys:

            toy['name'] = toy['name'][:50]  # Ограничиваем длину до 50 символов
            # Обновляем или создаём запись для каждой игрушки
            toy_instance, _ = LegoToy.objects.update_or_create(
                name=toy['name'],  # Уникальный идентификатор игрушки — имя
                defaults={
                    'age': toy['age'],
                    'pieces': toy['pieces'],
                    'rating': toy['rating'],
                    'price': toy['price'],
                    'discount': toy['discount'],
                    'description': toy['description'],
                }
            )
            existing_toy_ids.append(toy_instance.id)

        # Удаляем toys, которых больше нет на сайте
        LegoToy.objects.exclude(id__in=existing_toy_ids).delete()
