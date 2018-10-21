import FP_1_P96074105 as fpg
import csv

with open(r'F:\Data mining HW1\data\WoW Demographics.csv', newline='') as csvfile:
      rows = csv.reader(csvfile)	
      dataset = []
      for row in rows:
          dataset.append (row)

if __name__ == '__main__':
    frequent_itemsets = fpg.find_frequent_itemsets(dataset, minimum_support=10, include_support=True)
    print(type(frequent_itemsets))  
    result = []
    for itemset, support in frequent_itemsets:    
        result.append((itemset, support))

    result = sorted(result, key=lambda i: i[0])   
    for itemset, support in result:
        print(str(itemset) + ' ' + str(support))



