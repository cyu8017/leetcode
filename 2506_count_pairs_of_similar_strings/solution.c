// LeetCode 2506 - Count Pairs Of Similar Strings
// https://leetcode.com/problems/count-pairs-of-similar-strings/

#include <string.h>

int similarPairs(char** words, int wordsSize) {
    int masks[100];
    int freq[100];
    int mc = 0;
    int ans = 0;
    for (int wi = 0; wi < wordsSize; wi++) {
        int mask = 0;
        for (char* p = words[wi]; *p; p++) mask |= 1 << (*p - 'a');
        int found = -1;
        for (int i = 0; i < mc; i++) if (masks[i] == mask) { found = i; break; }
        if (found >= 0) {
            ans += freq[found];
            freq[found]++;
        } else {
            masks[mc] = mask;
            freq[mc] = 1;
            mc++;
        }
    }
    return ans;
}
