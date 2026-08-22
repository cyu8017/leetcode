// LeetCode 2399 - Check Distances Between Same Letters
// https://leetcode.com/problems/check-distances-between-same-letters/

#include <stdbool.h>

bool checkDistances(char* s, int* distance, int distanceSize) {
    (void)distanceSize;
    int first[26];
    for (int i = 0; i < 26; i++) first[i] = -1;
    for (int i = 0; s[i]; i++) {
        int c = s[i] - 'a';
        if (first[c] == -1) first[c] = i;
        else if (i - first[c] - 1 != distance[c]) return false;
    }
    return true;
}
