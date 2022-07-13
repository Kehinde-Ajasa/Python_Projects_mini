"""This module is used for calculating various statistical values like mean,
meadian, mode and range of data set"""


class CentralTendency:

	def mean(self, *val):
		number_list = list(val)
		length_of_numbers = len(number_list)
		sum_of_numbers = sum(number_list)
		mean = sum_of_numbers / length_of_numbers
		return f'The mean of the following numbers {val} is {round(mean, 2)}'

	def mode(self, *val):
		num_occurence = dict()
		number_list = list(val)
		item_list = list()
		mode_box = list()
		for i in number_list:
			if str(i) in num_occurence:
				num_occurence[str(i)] += 1
			else:
				num_occurence[str(i)] = 1
		for i in num_occurence:
			item_list.append(num_occurence[i])
		item_list.sort()
		for i in num_occurence:
			if num_occurence[i] == item_list[-1]:
				mode_box.append(i)
		if len(mode_box) == 1:
			return f'The Mode of the given numbers {val} is {"".join(mode_box)}'
		else:
			return f'This Data set has no Mode'

	def median(self, *val):
		ascending_order = list(val)
		ascending_order.sort()
		length_of_list = len(ascending_order)

		# When Length is Odd
		if length_of_list % 2 == 1:
			index_of_mid_number = int(length_of_list / 2)
			middle_number = ascending_order[index_of_mid_number]
			return f'The Median of the the given set of values {ascending_order} is {middle_number}'

		# When Length is Even
		else:
			index_of_mid_number = int(length_of_list / 2)
			middle_number = ascending_order[(index_of_mid_number - 1):(index_of_mid_number + 1)]
			result = sum(middle_number) / 2
			return f'The Median of the given set of values {ascending_order} is {result}'

	def range(self, *val):
		ordered_values = list(val)
		ordered_values.sort()
		result = ordered_values[-1] - ordered_values[0]
		return f'The range of the given set of values {ordered_values} is {result}'

Statistics = CentralTendency()
print(Statistics.mean(5, 3, 2, 3, 4, 5, 6, 7, 7, 8, 9, 4, 5))
print(Statistics.mode(5, 3, 2, 3, 4, 5, 6, 7, 7, 8, 9, 4, 5))
print(Statistics.median(10, 11, 12, 9, 8, 7, 13, 6, 4, 5, 2, 3, 1,))
print(Statistics.range(10, 11, 12, 9, 8, 7, 13, 6, 4, 5, 2, 3, 1,))
