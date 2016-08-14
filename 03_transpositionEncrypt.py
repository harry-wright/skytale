def main():

     # Message is 30 characters.
     
     myMessage = 'Begin each day by telling yourself: Today I shall be meeting with interference, ingratitude, insolence, disloyalty, ill-will, and selfishness – all of them due to the offenders’ ignorance of what is good or evil. But for my part I have long perceived the nature of good and its nobility, the nature of evil and its meanness, and also the nature of the culprit himself, who is my brother (not in the physical sense, but as a fellow creature similarly endowed with reason and a share of the divine); therefore none of those things can injure me, for nobody can implicate me in what is degrading.'
     myKey = 8
     
     # Passing values to encryptMessage function.

     ciphertext = encryptMessage(myKey, myMessage)

     # Shows output in tags.
     # This way if there is a space at the end, we know.
     
     print('<encrypted>' + ciphertext + '</encrypted>')

def encryptMessage(key, message):

     # Each item represents a column in the grid.
     # In this case, the key is 8. So 8 columns are made.
     # ['', '', '', '', '', '', '', ''].
     
     generatedtext = [''] * key
     
     # Range of key is (0,8).
     
     for col in range(key):
     
         # This pointer = 0, 1, 2, 3, 4, 5, 6, 7.
         
         pointer = col
         
         # Keep looping until pointer goes past 30.
         
         while pointer < len(message):
         
             # Add character at pointer to column.
             # First loop, generatedtext[0] += message[0]
             # Second, generatedtext[0] += message[8]
             
             generatedtext[col] += message[pointer]

             # Move pointer. First loop would be 0 to 8.
             
             pointer += key

     # Join the columns.
     
     return ''.join(generatedtext)

# Starts script at given point if not imported.

if __name__ == '__main__':
     main()