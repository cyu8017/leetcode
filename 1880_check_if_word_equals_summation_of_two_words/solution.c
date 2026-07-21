// LeetCode 1880 - Check if Word Equals Summation of Two Words
// https://leetcode.com/problems/check-if-word-equals-summation-of-two-words/

#include <stdbool.h>

static int wordValue(char* word) {
    int value = 0;
    for (int i = 0; word[i]; i++) value = value * 10 + (word[i] - 'a');
    return value;
}

bool isSumEqual(char* firstWord, char* secondWord, char* targetWord) {
    return wordValue(firstWord) + wordValue(secondWord) == wordValue(targetWord);
}
