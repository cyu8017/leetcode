// LeetCode 0792 - Number of Matching Subsequences
#include <stdlib.h>
#include <string.h>

int numMatchingSubseq(char* s, char** words, int wordsSize) {
    int count = 0;
    for (int w = 0; w < wordsSize; w++) {
        char* word = words[w];
        int i = 0, j = 0, n = (int)strlen(s), m = (int)strlen(word);
        while (i < n && j < m) {
            if (s[i] == word[j]) j++;
            i++;
        }
        if (j == m) count++;
    }
    return count;
}
