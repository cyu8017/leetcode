// LeetCode 3042 - Count Prefix and Suffix Pairs I
// https://leetcode.com/problems/count-prefix-and-suffix-pairs-i/

#include <string.h>
#include <stdbool.h>

static bool isPrefixSuffix(const char* t, const char* s) {
    int nt = (int)strlen(t), ns = (int)strlen(s);
    if (ns > nt) return false;
    if (strncmp(t, s, ns) != 0) return false;
    return strncmp(t + nt - ns, s, ns) == 0;
}

int countPrefixSuffixPairs(char** words, int wordsSize) {
    int ans = 0;
    for (int i = 0; i < wordsSize; i++) {
        for (int j = i + 1; j < wordsSize; j++) {
            if (isPrefixSuffix(words[j], words[i])) ans++;
        }
    }
    return ans;
}
