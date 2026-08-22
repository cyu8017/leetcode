// LeetCode 2531 - Make Number of Distinct Characters Equal
// https://leetcode.com/problems/make-number-of-distinct-characters-equal/

#include <stdbool.h>
#include <string.h>

bool isItPossible(char* word1, char* word2) {
    int c1[26] = {0}, c2[26] = {0};
    for (int i = 0; word1[i]; i++) c1[word1[i] - 'a']++;
    for (int i = 0; word2[i]; i++) c2[word2[i] - 'a']++;
    int d1 = 0, d2 = 0;
    for (int i = 0; i < 26; i++) {
        if (c1[i] > 0) d1++;
        if (c2[i] > 0) d2++;
    }
    for (int a = 0; a < 26; a++) {
        if (!c1[a]) continue;
        for (int b = 0; b < 26; b++) {
            if (!c2[b]) continue;
            int nd1 = d1, nd2 = d2;
            if (a == b) {
                if (nd1 == nd2) return true;
                continue;
            }
            if (c1[a] == 1) nd1--;
            if (c1[b] == 0) nd1++;
            if (c2[b] == 1) nd2--;
            if (c2[a] == 0) nd2++;
            if (nd1 == nd2) return true;
        }
    }
    return false;
}
