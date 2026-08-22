// LeetCode 0408 - Valid Word Abbreviation
// https://leetcode.com/problems/valid-word-abbreviation/

#include <ctype.h>
#include <stdbool.h>
#include <string.h>

bool validWordAbbreviation(char* word, char* abbr) {
    int wordIndex = 0;
    int abbrIndex = 0;
    int wordLength = (int)strlen(word);
    int abbrLength = (int)strlen(abbr);

    while (wordIndex < wordLength && abbrIndex < abbrLength) {
        if (isdigit((unsigned char)abbr[abbrIndex])) {
            if (abbr[abbrIndex] == '0') {
                return false;
            }

            int number = 0;
            while (abbrIndex < abbrLength && isdigit((unsigned char)abbr[abbrIndex])) {
                number = number * 10 + (abbr[abbrIndex] - '0');
                abbrIndex += 1;
            }
            wordIndex += number;
        } else {
            if (word[wordIndex] != abbr[abbrIndex]) {
                return false;
            }
            wordIndex += 1;
            abbrIndex += 1;
        }
    }

    return wordIndex == wordLength && abbrIndex == abbrLength;
}
