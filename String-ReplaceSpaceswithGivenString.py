#Replace all Spaces with Given String
main_string = input("Please Enter main string")
string_to_be_inserted = input("Please Enter a word you want space to replace with")

def replace_spaces_with_given_string(main_string,string_to_be_inserted):
    return main_string.replace(" " , string_to_be_inserted)

print(replace_spaces_with_given_string(main_string,string_to_be_inserted))