plain_text = str(input("Masukan Teks: "))
key_plain_text = str(input("Masukan Key: "))

def binary_to_matrix(plain_text):

    def make_to_8_bit(str_bin):
        while len(str_bin) < 8:
            str_bin = "0"+str_bin
        return str_bin
    
    cache_arr = []
    for word in plain_text:
        
        to_ascii = ord(word)
        to_binary = bin(to_ascii).replace('0b','')

        convert_to_8bit = make_to_8_bit(to_binary)
        convert_bin_to_arr = list(convert_to_8bit)

        cache_arr.append(convert_bin_to_arr)

    plain_text_arr = []
    for i in range(0, len(cache_arr), 8):
        plain_text_arr.append(cache_arr[i:i+8])
    return plain_text_arr

def ip_generator(arr):

    cache_arr_ip = []
    for j in range(1, 8, 2):
        for i in range(0, 8, 1):
            row = len(arr)-1 - i
            cache_arr_ip.append(arr[row][j])    

    for j in range(0, 7, 2):
        for i in range(0, 8, 1):
            row = len(arr)-1 - i
            cache_arr_ip.append(arr[row][j])

    cache_final_arr_ip = []
    for z in range(0, len(cache_arr_ip), 8):
        cache_final_arr_ip.append(cache_arr_ip[z:z+8])
    return cache_final_arr_ip

def c_d_generator(arr):
    c_arr = []
    for j in range(0, 8, 1):
        column = j
        for i in range(0, 8, 1):
            row = 7-i
            c_arr.append(arr[row][column])
            if column == 3 and row == 4:
                break
        if column == 3 and row == 4:
            break
    final_arr_c = []

    for x in range(0, len(c_arr), 7):
        final_arr_c.append(c_arr[x:x+7])


    #===========================
    d_arr = []
    for m in range(1, len(arr), 1):
        col = 7-m
        for v in range(0, len(arr), 1):
            row = 7-v
            if col == 3 and row >= 4:
                continue
            d_arr.append(arr[row][col]) 
            if row == 0 and col == 3:
                break
        if row == 0 and col == 3:
            break

    final_arr_d = []
    for x in range(0, len(d_arr), 7):
        final_arr_d.append(d_arr[x:x+7])

    return [final_arr_c, final_arr_d]

plain_text_matrix = binary_to_matrix(plain_text)
key_matrix = binary_to_matrix(key_plain_text)[0]

ip_plain_matrix = ip_generator(plain_text_matrix[0])
c_d_key_matrix = c_d_generator(key_matrix)

print(c_d_key_matrix)