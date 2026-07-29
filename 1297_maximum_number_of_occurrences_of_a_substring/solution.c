// LeetCode 1297 - Maximum Number of Occurrences of a Substring
// https://leetcode.com/problems/maximum-number-of-occurrences-of-a-substring/

#include <string.h>

int maxFreq(char* s, int maxLetters, int minSize, int maxSize) {
    (void)maxSize;
    int n = (int)strlen(s);
    int freq[70000] = {0};
    int best = 0;
    for (int i = 0; i + minSize <= n; i++) {
        int letters = 0;
        int seen[26] = {0};
        for (int j = i; j < i + minSize; j++) {
            if (!seen[s[j] - 'a']) {
                seen[s[j] - 'a'] = 1;
                letters++;
            }
        }
        if (letters > maxLetters) continue;
        int hash = 0;
        for (int j = i; j < i + minSize; j++) hash = hash * 27 + (s[j] - 'a' + 1);
        freq[hash]++;
        if (freq[hash] > best) best = freq[hash];
    }
    return best;
}
