// LeetCode 1100 - Find K-Length Substrings With No Repeated Characters
// https://leetcode.com/problems/find-k-length-substrings-with-no-repeated-characters/

#include <string.h>

int numKLenSubstrNoRepeats(char* s, int k) {
    int n = (int)strlen(s);
    if (k > n) return 0;
    int freq[256] = {0};
    int distinct = 0;
    for (int i = 0; i < k; i++) {
        if (freq[(unsigned char)s[i]]++ == 0) distinct++;
    }
    int ans = distinct == k;
    for (int i = k; i < n; i++) {
        if (freq[(unsigned char)s[i]]++ == 0) distinct++;
        if (--freq[(unsigned char)s[i - k]] == 0) distinct--;
        if (distinct == k) ans++;
    }
    return ans;
}
