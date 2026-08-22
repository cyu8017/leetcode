// LeetCode 0422 - Valid Word Square
// https://leetcode.com/problems/valid-word-square/

#include <stdbool.h>
#include <string.h>

bool validWordSquare(char** words, int wordsSize) {
    for (int row = 0; row < wordsSize; row++) {
        int wordLen = (int)strlen(words[row]);
        for (int col = 0; col < wordLen; col++) {
            if (col >= wordsSize || row >= (int)strlen(words[col]) || words[col][row] != words[row][col]) {
                return false;
            }
        }
    }
    return true;
}
