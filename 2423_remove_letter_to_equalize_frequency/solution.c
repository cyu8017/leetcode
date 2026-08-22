// LeetCode 2423 - Remove Letter To Equalize Frequency
// https://leetcode.com/problems/remove-letter-to-equalize-frequency/

#include <stdbool.h>
#include <string.h>

bool equalFrequency(char* word) {
    int n = (int)strlen(word);
    for (int skip = 0; skip < n; skip++) {
        int cnt[26] = {0};
        for (int i = 0; i < n; i++) if (i != skip) cnt[word[i] - 'a']++;
        int freqVal = -1; bool ok = true; bool have = false;
        for (int i = 0; i < 26; i++) if (cnt[i] > 0) {
            if (!have) { freqVal = cnt[i]; have = true; }
            else if (cnt[i] != freqVal) { ok = false; break; }
        }
        if (ok && have) return true;
    }
    return false;
}
