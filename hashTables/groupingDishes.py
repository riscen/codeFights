#Ugly solution O(n^2 + n)
def groupingDishes(dishes):
    ingredientsSet = set()
    ingredients = []
    dishGroups = []
    for dish in dishes:
        for i in range(1, len(dish)):
            if not dish[i] in ingredientsSet:
                ingredientsSet.add(dish[i])
                index = len(dishGroups)
                for j in range(len(dishGroups)):
                    if dish[i] < dishGroups[j][0]:
                        index = j
                        break
                dishGroups.insert(index, [dish[i], dish[0]])
            else:
                for group in dishGroups:
                    if group[0] == dish[i]:
                        group.insert(getSortedIndex(1, dish[0], group), dish[0])
    i = 0
    while i < len(dishGroups):
        if len(dishGroups[i]) == 2:
            dishGroups.remove(dishGroups[i])
            i -= 1
        i += 1
    return dishGroups


def getSortedIndex(beginIndex, value, array):
    for i in range(beginIndex, len(array)):
        if value < array[i]:
            return i
    return len(array)
        
        