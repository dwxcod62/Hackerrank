There is a sentence that consists of space-separated strings of upper and lower case English letters. Transform each string according to the given algorithm and return the new sentence.

Each string should be modified as follows:

-   The first character of the string remains unchanged

-   For each subsequent character, say x, consider a letter
    preceding it, say y:
    -   If y precedes x in the English alphabet, transform x to uppercase
    -   If x precedes y in the English alphabet, transform x to lowercase
    -   If x and y are equal, the letter remains unchanged

**Example**

_sentence = "cOOL dog"_

The first letters of both words remain unchanged. Then, for the word "COOL" the first "o" is made uppercase because the letter preceding it, "c", comes earlier in the alphabet. Next, the case of the second "O" is unchanged because the letter preceding is also "o", and finally the "L" is made lowercase because the letter preceding it, "O", comes later in the alphabet. The second word, "dOg", is transformed according to the same rules. Return the resulting sentence 'cool dog'.

**Function Description**

Complete the function _transformSentence_ in the editor below. The function must return a string representing the resulting sentence.

_transformSentence_ has the following parameter(s): string sentence: the input sentence
