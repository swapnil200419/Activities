"""
Suppose you are buying something online on amazon.com
On the website, you get a 15% discount if you are a prime member. Additionally, you are also getting a discount of 8% on the item because it's black Friday sales.
Write a function that takes as input the amount of the asset that you are buying and a logical variable indicating whether you are a prime member applies the discount offered appropriately and returns the result.
"""

a=float(input("Enter Amount: "))
b=input('Are you a Prime member : ')
def discount(a,b):
    if b=='yes' or b=='Yes' or b=='YES':
        d1=0.15*a
        c=a-d1
        bfd=0.08*c
        f_p=c-bfd
        return (f_p)
    else:
        s=0.08*a
        r=a-s
        return(r)
print(discount(a,b)

"""
In few chit-chat programs, there is a limitation on the number of letters that you can send to your family and friends.
Write a function that takes as input the,
message and checks whether the number of letters is less than 200 or above. If the length of the information is less than 200, the chat should be returned.
If the length of the chat is greater than 200, data consisting of only the first 200 characters should be returned.
"""

a=input()
def chat(a):
    if len(a)<=200:
        return a
    else:
        b=a[:200]
        return b
print(chat(a)

"""
(b) How one can check if the restriction is on a number of words rather than letters? Write a function that allows a message with only 30 words
"""

def length(msg):
    if len(msg) <= 200:
        return msg
    else:
        return msg[:200]
print(msg_length(''))
def msg_word_count(msg):
    words = msg.split()
    if len(words) <= 30:
        return msg
    else:
        return "Message should not contain more than 30 words."