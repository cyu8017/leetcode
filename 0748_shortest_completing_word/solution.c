// LeetCode 0748 - Shortest Completing Word
// https://leetcode.com/problems/shortest-completing-word/

#include <ctype.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

char* shortestCompletingWord(char* licensePlate, char** words, int wordsSize) {
    int need[26] = {0};
    for (char* p = licensePlate; *p; p++) {
        if (isalpha((unsigned char)*p)) {
            need[tolower((unsigned char)*p) - 'a']++;
        }
    }
    char* best = NULL;
    for (int w = 0; w < wordsSize; w++) {
        int counts[26] = {0};
        for (char* p = words[w]; *p; p++) {
            if (isalpha((unsigned char)*p)) {
                counts[tolower((unsigned char)*p) - 'a']++;
            }
        }
        bool ok = true;
        for (int i = 0; i < 26; i++) {
            if (counts[i] < need[i]) {
                ok = false;
                break;
            }
        }
        if (ok && (!best || strlen(words[w]) < strlen(best))) {
            best = words[w];
        }
    }
    if (!best) {
        char* empty = (char*)malloc(1);
        empty[0] = '\0';
        return empty;
    }
    char* out = (char*)malloc(strlen(best) + 1);
    strcpy(out, best);
    return out;
}
