# def parse_encoded_string(encoded_str):
#     # data_parts = encoded_str.split('0')
#     data_parts=[]
#     for i in encoded_str.split('0'):
#         if i:
#             data_parts.append(i)
#     first_name = data_parts[0]
#     last_name = data_parts[1]
#     id = data_parts[2]
#     result = {
#         "first_name": first_name,
#         "last_name": last_name,
#         "id": id
#     }
#     return result
# input_string="Aman000Tiwari0000906"
# parsed_data = parse_encoded_string(input_string)
# print(parsed_data)

# user="dhruvi00000virani0012345"
# empty_dict={}
# split=[]
# for i in user.split('0'):
#     if i:
#         split.append(i)
# print(split)
# empty_dict['Firstname']=split[0]
# empty_dict['Lastname']=split[1]
# empty_dict['ID']=split[2]
# print(empty_dict)


# def has_duplicate_letters(sentence):
#     words = sentence.split()
#
#     for word in words:
#         unique_letters = set()
#
#         for letter in word:
#
#             if letter in unique_letters:
#                 return True
#             else:
#                 unique_letters.add(letter)
#     return False
#
# sentence1 = "This is a test sentence"
# sentence2 = "Aman"
# sentence3 = "Python programming"
# print(has_duplicate_letters(sentence1))
# print(has_duplicate_letters(sentence2))
# print(has_duplicate_letters(sentence3))

# a="This is a sample sentence to check redundancy"
# b=set(a)

def duplicate(a):
    b = set(a)
    if len(a)==len(b):
        print("False, this dont have any duplicate letters")
        return True
    else:
        print("True, this sentence has duplicate letters")
    return False
c="This is a sample sentence"
duplicate(c)















