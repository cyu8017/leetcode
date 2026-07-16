// LeetCode 0418 - Sentence Screen Fitting
// https://leetcode.com/problems/sentence-screen-fitting/

#include <string.h>

int wordsTyping(char** sentence, int sentenceSize, int rows, int cols) {
    int count = 0;
    int index = 0;

    for (int row = 0; row < rows; row++) {
        int col = 0;
        while (1) {
            char* word = sentence[index];
            int needed = (int)strlen(word) + (col > 0 ? 1 : 0);
            if (col + needed > cols) {
                break;
            }
            if (col > 0) {
                col++;
            }
            col += (int)strlen(word);
            index = (index + 1) % sentenceSize;
            if (index == 0) {
                count++;
            }
        }
    }

    return count;
}
