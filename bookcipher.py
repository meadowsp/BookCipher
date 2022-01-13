""" Performs the Book Cipher.

arguments:
  -h, --help            show this help message and exit
  -m {encipher,e,unencipher,u}, --mode {encipher,e,unencipher,u}
                        Mode: encipher or unencipher
  -b BOOKFILENAME, --bookfilename BOOKFILENAME
                        Book filename
  -i INPUTFILENAME, --inputfilename INPUTFILENAME
                        Input file to be processed
  -o OUTPUTFILENAME, --outputfilename OUTPUTFILENAME
                        Output file to be created
"""
import argparse
import json
import random

def encipher(sourcemessagefilename, bookfilename, outputfilename):
    """Enciphers a message to an output file using a book

    Args:
        sourcemessagefilename (str): Filename of the message to encipher
        bookfilename (str): Filename of the book to use as the key
        outputfilename (str): Filename of the file to store the enciphered message

    Raises:
        ValueError: If there is a character in the source message that doesn't exist in the book
    """

    print("Enciphering message : " + sourcemessagefilename)
    print("Using book          : " + bookfilename)
    print("Output to           : " + outputfilename)

    with open(sourcemessagefilename, "rt", encoding="utf-8") as sf, open(bookfilename, "rt", encoding="utf-8") as bkf:

        # Get the size of the book

        booktext = bkf.read()
        booksize = len(booktext)

        enciphered = []
        sourceText = sf.read()

        for sourcechar in sourceText:

            # to avoid picking the same position for each character every time, start from a random position,
            # search to the end, and then, if still not found, search from the start of the file to the initial search start position

            startpos = random.randrange(booksize)

            charpos = booktext.index(sourcechar, startpos)
            if (charpos == -1):
                charpos = booktext.index(sourcechar, 0, startpos)

            if (charpos == -1):
                raise ValueError("Character : " + sourcechar +
                                 ", was not found in the book")

            enciphered.append(charpos)

    with open(outputfilename, "wt") as of:
        json.dump(enciphered, of)

    print("Enciphering completed.")
    return


def unencipher(encipheredmessagefilename, bookfilename, unencipheredmessagefilename):

    """Unenciphers an enciphered message to an plain text message using a book

    Args:
        sourcemessagefilename (str): Filename of the enciphered message
        bookfilename (str): Filename of the book to use as the key
        outputfilename (str): Filename of the file to store the plaintext message

    """
 
    print("Unenciphering message : " + encipheredmessagefilename)
    print("Using book            : " + bookfilename)
    print("Output to             : " + unencipheredmessagefilename)

    unencipheredmsg = []

    with open(encipheredmessagefilename, "rt") as ef, open(bookfilename, "rt", encoding="utf-8") as bkf:
        enciphered = json.load(ef)
        booktext = bkf.read()
        for encipheredpos in enciphered:
            unencipheredmsg.append(booktext[encipheredpos])

    with open(unencipheredmessagefilename, "wt", encoding='UTF-8') as uf:
        uf.write("".join(unencipheredmsg))

    print("Unenciphering completed.")

    return

def display_banner():
    """Displays the banner."""
    name = '''    
    ____                   __            ______    _              __                
   / __ )  ____   ____    / /__         / ____/   (_)    ____    / /_   ___    _____
  / __  | / __ \ / __ \  / //_/        / /       / /    / __ \  / __ \ / _ \  / ___/
 / /_/ / / /_/ // /_/ / / ,<          / /___    / /    / /_/ / / / / //  __/ / /    
/_____/  \____/ \____/ /_/|_|         \____/   /_/    / .___/ /_/ /_/ \___/ /_/     
                                                     /_/                            

    '''
    print(name)
    return

def main(args):
    """Main processing function"""
    display_banner()
    if (args.mode == 'encipher' or args.mode == 'e'):
        encipher(args.inputfilename, args.bookfilename, args.outputfilename)
    else:
        unencipher(args.inputfilename, args.bookfilename, args.outputfilename)
    return

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Book Cipher')
    required = parser.add_argument_group('required arguments')
    required.add_argument('-m', '--mode', choices=['encipher', 'e', 'unencipher', 'u'],
                        help='Mode: encipher or unencipher', required=True, dest='mode')

    required.add_argument("-b", "--bookfilename",
                        help="Book filename", required=True, dest='bookfilename')

    required.add_argument("-i", "--inputfilename",
                        help="Input file to be processed", required=True, dest='inputfilename')

    required.add_argument("-o", "--outputfilename",
                        help="Output file to be created", required=True, dest='outputfilename')

    main(parser.parse_args())


# Example uses
# & C:/Users/meado/AppData/Local/Microsoft/WindowsApps/python3.9.exe c:/dev/BookCipher/bookcipher.py -m e -b KingJamesBible.txt -i sourcemessage.txt -o output.txt
# & C:/Users/meado/AppData/Local/Microsoft/WindowsApps/python3.9.exe c:/dev/BookCipher/bookcipher.py -m u -b KingJamesBible.txt -i output.txt -o unenciphered.txt
