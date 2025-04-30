from typing import List

#Skeleton code for even_list
sum = 0
even_int_list =[]
def even_list(int_list):
    for i in range(len(int_list)):
        if int_list[i] % 2 == 0:
            even_int_list.append(int_list[i])
    # TODO: Implement even_list
    
#Skeleton code for sum_of_squares_of_even
def sum_of_squares_of_even(even_int_list:List[int]) -> int:
    """"
    Computes the sum of the squares of all even numbers in a list of integers.
    
    Args:
        even_int_list: A list of even integers.
        
    Retruns:
        The sum of the squares of all even numbers in the list.
        """
        #TODO: Implement sum_of_squares_of_even
        pass
    
    #Main function
    def main():
        #Example list
        int_list = [1,2,3,4,5,6,7,8,9,10]
        even_int_list = even_list(int_list)
        output = sum_of_squares_of_even(even_int_list)
        print(output)
        
        #Boilerplate code
        if__name__=="_main_":
main()
        
