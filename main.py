class cookbook():
    def __init__(self):
        self.book = {}
        self.dishes = []
        self.person_count = 0
        self.shop_list = {}

# Заполнение книги данными из файла установленной структуры
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

# Формирование списка покупок
    def get_shop_list_by_dishes(self, dishes, person_count):
        del self.dishes[:]
        self.dishes.extend(dishes)
        self.person_count = person_count
        self.shop_list.clear()
        for dish in self.dishes:
            if dish in self.book.keys():
                for ingredient in self.book[dish]:
                    if ingredient['ingredient_name'] in self.shop_list.keys() and self.shop_list[ingredient['ingredient_name']]['measure'] == ingredient['measure']:
                        self.shop_list[ingredient['ingredient_name']]['quantity'] += ingredient['quantity'] * person_count
                    else :
                        self.shop_list.setdefault(ingredient['ingredient_name'], {'measure': ingredient['measure'], 'quantity': ingredient['quantity'] * person_count})
        newstring = ''
        for key, value in self.shop_list.items():
            newstring += key + " : " + str(value) + '\n'
        return newstring

# Переопределение печати книги рецептов
    def __str__(self):
        newstring = ''
        for dish, ingredients in self.book.items():
            newstring += dish + '\n'
            for ingredient in ingredients:
                newstring += str(ingredient) + '\n'
        return newstring


# Основной код
my_cookbook = cookbook()
my_cookbook.fill_book("recipes.txt")
print(my_cookbook)
print(my_cookbook.get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
print(my_cookbook.shop_list)