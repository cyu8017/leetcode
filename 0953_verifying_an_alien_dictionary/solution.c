// LeetCode 0953 - Verifying an Alien Dictionary
// https://leetcode.com/problems/verifying-an-alien-dictionary/

#include <stdbool.h>
#include <string.h>

bool isAlienSorted(char** words, int wordsSize, char* order) {
    int rank[26];
    for (int i = 0; i < 26; i++) rank[order[i] - 'a'] = i;
    for (int i = 0; i + 1 < wordsSize; i++) {
        char *a = words[i], *b = words[i + 1];
        int j = 0;
        while (a[j] && b[j] && a[j] == b[j]) j++;
        if (!b[j] && a[j]) return false;
        if (a[j] && b[j] && rank[a[j] - 'a'] > rank[b[j] - 'a']) return false;
    }
    return true;
}
