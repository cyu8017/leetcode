// LeetCode 1160 - Find Words That Can Be Formed by Characters
// https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/

#include <string.h>

int countCharacters(char** words, int wordsSize, char* chars) {
    int avail[26] = {0};
    for (char* p = chars; *p; p++) avail[*p - 'a']++;
    int ans = 0;
    for (int w = 0; w < wordsSize; w++) {
        int need[26] = {0};
        int ok = 1, len = 0;
        for (char* p = words[w]; *p; p++) { need[*p - 'a']++; len++; }
        for (int i = 0; i < 26; i++) if (need[i] > avail[i]) { ok = 0; break; }
        if (ok) ans += len;
    }
    return ans;
}
