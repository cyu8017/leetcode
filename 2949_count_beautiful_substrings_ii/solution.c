// LeetCode 2949 - Count Beautiful Substrings II
// https://leetcode.com/problems/count-beautiful-substrings-ii/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

static bool isVowel(char c) {
    return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
}

typedef struct { int bal, mod, cnt; } Key;

long long beautifulSubstrings(char* s, int k) {
    int x = 1;
    while ((x * x) % k != 0) x++;
    int n = (int)strlen(s);
    Key* freq = (Key*)malloc((n + 2) * sizeof(Key));
    int fn = 0;
    freq[fn++] = (Key){0, 0, 1};
    int bal = 0, vowels = 0;
    long long ans = 0;
    for (int i = 0; i < n; i++) {
        if (isVowel(s[i])) { bal++; vowels++; }
        else bal--;
        int mod = vowels % x;
        int found = -1;
        for (int j = 0; j < fn; j++) if (freq[j].bal == bal && freq[j].mod == mod) { found = j; break; }
        if (found >= 0) { ans += freq[found].cnt; freq[found].cnt++; }
        else { freq[fn++] = (Key){bal, mod, 1}; }
    }
    free(freq);
    return ans;
}
