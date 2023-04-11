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