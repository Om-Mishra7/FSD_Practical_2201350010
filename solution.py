# Write a Program to implement a generator which prints all even numbers between 0 and 20

def even_generator():

    for i in range(2, 21, 2): # This is a genrator function that yields value between 2 and 20 with an increment of 2
       
        yield i  # yield keyword is used to return a value from a generator function

if __name__ == "__main__":
    
    for i in even_generator(): # This is a for loop to iterate over the generator object and print the values only if the file is run directly
        print(i)