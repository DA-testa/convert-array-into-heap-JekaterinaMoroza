# python3


def build_heap(data):
    n = len(data)
    swaps = []
    def sift_down(i):
        min_index= i
        right_child= 2*i+2
        left_child= 2*i+1
        
        if left_child < len(data) and data[left_child] < data [min_index]:
            min_index= left_child

        if right_child < len(data) and data[right_child] < data [min_index]:
            min_index= right_child

        if i != min_index:
            data[i], data[min_index] = data[min_index], data[i]
            swaps.append((i, min_index))
            sift_down(min_index)


    for i in range (n//2, -1, -1):
        sift_down(i)

    return swaps


def main():
    
    inputs = input("Izvēlies I vai F: ")
    if "I" in inputs:
        n = int(input("Ievadi daudzumu: "))
        data = list(map(int, input("Ievadi skaitļus: ").split()))

    # checks if lenght of data is the same as the said lenght
    elif "F" in inputs:

        filename = input("Faila nosaukums: ")
        with open("tests/"+filename, 'r') as f:
            n = int(f.readline())
            data = list(map(int, f.readline().split()))

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
