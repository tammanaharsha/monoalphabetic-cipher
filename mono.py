import sys
import random

# Define the characters we want to encode from a to z and 0 to 9
main = [chr(i) for i in range(ord('a'), ord('z')+1)] + \
           [str(i) for i in range(10)]

# Create a function to generate the mapping by using seed and returning our_test and enct_test
def generate_mapping(seedkey):
    # Create a list of characters and shuffle it with the given seed
    mono_cipher = list(main)
    random.seed(seedkey)
    random.shuffle(mono_cipher)
    # Create arrays to store the mapping
    our_tests = list(main)
    enct_test = mono_cipher
    return our_tests, enct_test

# Create a function to perform encryption or decryption with operation 0 or 1 (0 for decryption, 1 for encryption)
def encrypt_decrypt(our_text, enc_text, our_tests, enct_test, testingnum):
    # Create dictionaries to store the mapping
    if testingnum == 1:
        mapping = dict(zip(our_tests, enct_test))
    else:
        mapping = dict(zip(enct_test, our_tests))
    with open(our_text, 'r') as f_in:
        with open(enc_text, 'w') as f_out:
            while True:
                char = f_in.read(1)
                if not char:
                    break
                f_out.write(mapping.get(char, char))

# Read the arguments from the command line for input file, output file, seed and operation
if len(sys.argv) != 5:
    print("Please provide input file, output file, seed, and operation.")
    sys.exit(1)

our_text = sys.argv[1]
enc_text = sys.argv[2]
seed = int(sys.argv[3])
testingnum = int(sys.argv[4])

# Validate the seed value
if seed < 50 or seed > 10000:
    print("Invalid seed value. The seed value should be between 50 and 10000.")
    sys.exit(1)

# Get the file extensions for the input and output files
input_ext = our_text.split('.')[-1]
output_ext = enc_text.split('.')[-1]

# If the input and output files do not have extensions, add them
if input_ext == our_text or output_ext == enc_text:
    our_text += '.txt'
    enc_text += '.txt'

if testingnum<0 or testingnum>1:
    print("the operation should be 0 or 1 zero for encryption one for decryption.")
    sys.exit(1)

if seed<50 or seed>10000 and testingnum<0 or testingnum>1:
    print("invalid seed value and invalid operation.")
    sys.exit(1)

# Generate the character mappings
our_tests, enct_test = generate_mapping(seed)

# Perform the encryption or decryption
encrypt_decrypt(our_text, enc_text, our_tests, enct_test, testingnum)

# Print the mappings for every character
mapping = dict(zip(our_tests, enct_test))
print(', '.join([f"{letter}-{itsmapping}" for letter, itsmapping in mapping.items()]))
