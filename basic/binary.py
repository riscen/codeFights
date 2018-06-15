def binarySearch(array, value):
	top = len(array)
	bottom = 0
	mid = int(top/2)
	while bottom < top:
		print('Bot: %d, Top: %d, Mid: %d, Val: %d' % (bottom, top, mid, array[mid]))
		if value == array[mid]:
			return mid
		elif value > array[mid]:
			bottom = mid
			mid += int((top-bottom)/2)
		else:
			top = mid
			mid -= int((top-bottom)/2)
	return -1

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
index = binarySearch(array, 5)
print('V: %d, I: %d' % (5, index))