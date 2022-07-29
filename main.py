# Функции
# создание кулинарной книги
class cookbook():
    def __init__(self):
        self.book = {}

    def fill_book(self, file_name):
        if len(self.book) > 0:
            return
        try:
            file_obj = open(file_name, 'r', encoding='utf-8')
        except Exception:
            return "There is no such file"
        else:
            with file_obj:
                while True:
                    dish = file_obj.readline().strip()
                    if len(dish) == 0:
                        break
                    num_of_ingredients = int(file_obj.readline().strip())
                    recipe = []
                    for record in range(0, num_of_ingredients):
                        ingredient = {}
                        read_string = file_obj.readline().strip().split('|')
                        ingredient['ingredient_name'] = read_string[0].strip()
                        ingredient['quantity'] = int(read_string[1])
                        ingredient['measure'] = read_string[2].strip()
                        recipe.append(ingredient)
                    self.book[dish] = recipe
                    file_obj.readline()

    def get_shop_list_by_dishes(self, dishes, person_count):
        shop_list = {}
        for dish in dishes:
            if dish in self.book.keys():
                print(dish)



# Расчёт ингредиентов




# Основной код
my_cookbook = cookbook()
my_cookbook.fill_book("recipes.txt")
print(my_cookbook.book)
my_cookbook.get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)