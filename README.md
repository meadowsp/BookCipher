# Book Cipher

## Description
Book Cipher is an implementation of a [Book Cipher](https://en.wikipedia.org/wiki/Book_cipher "Wikipedia Book Cipher article"), which uses a substitution cipher. Each character in the souce message to be enciphered is converted to the position (character offset) of an equivalent character in the book. To add an extra level of security, rather than just the first position for each character being used, the instance of the source character in the book will be selected randomly.

## Disclaimer
Do not use this for any serious purposes! No guarantees are made as to the security of this cipher. The golden security rule of **"Don't roll your own crypto"** still applies. This code is provided purely as an example.

## Usage
### Pre-requisites
This code requires Python 3.

You will also need a book to use as a key, a good candidate is the King James Bible available [here](https://www.gutenberg.org/ebooks/10) from Project Gutenberg. Download the UTF-8 text version. 

You will also need a message to encipher. An example is provided in this repo as `sourcemessage.txt`. Any other message you would like to use must be in UTF-8 format. The book must contain all of the characters in the message, otherwise an exception will be thrown.
### Use
```                         
usage: bookcipher.py [-h] -m {encipher,e,unencipher,u} -b BOOKFILENAME -i INPUTFILENAME -o OUTPUTFILENAME

Book Cipher

optional arguments:
  -h, --help            show this help message and exit

required arguments:
  -m {encipher,e,unencipher,u}, --mode {encipher,e,unencipher,u}
                        Mode: encipher or unencipher
  -b BOOKFILENAME, --bookfilename BOOKFILENAME
                        Book filename
  -i INPUTFILENAME, --inputfilename INPUTFILENAME
                        Input file to be processed
  -o OUTPUTFILENAME, --outputfilename OUTPUTFILENAME
                        Output file to be created                    
```

Assuming that you've downloaded the King James Bible and are using that as your book some example usages are below:

Enciphering a message and outputting the enciphered version to a file called `output.txt`.
```
python3 bookcipher.py -m e -b KingJamesBible.txt -i sourcemessage.txt -o output.txt
```

Unenciphering an enciphered message from the file calles `output.txt` and storing the plain text in `unenciphered.txt`.
```
python3 bookcipher.py -m u -b KingJamesBible.txt -i output.txt -o unenciphered.txt
```



