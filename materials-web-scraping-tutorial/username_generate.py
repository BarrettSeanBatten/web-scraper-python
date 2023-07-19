import random
import string

def generate_username(num_usernames=1, word_length=5, num_digits=3):
    usernames = []
    for _ in range(num_usernames):
        word = ''.join(random.choice(string.ascii_lowercase) for _ in range(word_length))
        digits = ''.join(random.choice(string.digits) for _ in range(num_digits))
        username = word + digits
        usernames.append(username)
    return usernames

if __name__ == "__main__":
    num_usernames_to_generate = 1000  # Change this value to generate more usernames
    generated_usernames = generate_username(num_usernames_to_generate)
    for username in generated_usernames:
        print(username)
