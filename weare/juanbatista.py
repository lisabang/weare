
flag = True
print("I'm a chatbot. Talk to me because you have no friends.")
print("The only way this pointless conversation is ending is if you tell me to go away!")

while flag == True:
    user_response = input()
    user_response = user_response.lower()
    if 'go away' == user_response:
        flag = False
    elif 'we are' in user_response:
        print("Penn State")
    elif 'ben shapiro' in user_response:
        print("His wife's a doctor. Did you know that?")
    else:
print("I'm much less gay than the dominos pizza bot.")
