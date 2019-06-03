from DTP_get_data import get_data
import datetime
import math
from random import shuffle
import pickle


def main():
	data_number = "0.3"
	sequence_dic, lable_dic, data_id, data_number = get_data(data_number)


	#print(sequence_dic)
	#print(lable_dic)
	print(data_id)
	print(len(data_id))
	print(type(data_id))

	train,val,test = select_train_val_test(data_id)
	print(len(train))
	print(len(val))
	print(len(test))
	print(type(train))
	f_train = open("redundancy_train.pickle", 'wb')
	f_val= open("redundancy_val.pickle", 'wb')
	f_test = open("redundancy_test.pickle", 'wb')
	pickle.dump(train, f_train)
	pickle.dump(val, f_val)
	pickle.dump(test, f_test)




def select_train_val_test(data_id):
	data_number = len(data_id)
	test_percent = 0.2
	val_percent = 0.1
	train = []
	val = []
	test = []

	test_data_number = math.ceil(data_number * test_percent)
	val_data_number = math.ceil(data_number * val_percent)
	print(test_data_number)
	print(val_data_number)

	x = [i for i in range(data_number)]
	shuffle(x)
	print(x)
	counter = 0
	for item in x:
		if counter <test_data_number:
			#print(item)
			test.append(data_id[item])
		elif counter >= test_data_number and counter < test_data_number + val_data_number:
			#print(item)
			val.append(data_id[item])
		else:
			#print(item)
			train.append(data_id[item])

		counter = counter + 1

	print(test)
	print(val)
	print(train)


	return train,val,test



if __name__ == "__main__":
	starttime = datetime.datetime.now()
	main()
	endtime = datetime.datetime.now()
	print("totaltime = " + str(endtime - starttime))













