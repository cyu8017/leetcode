// LeetCode 2606 - Find the Substring With Maximum Cost
// https://leetcode.com/problems/find-the-substring-with-maximum-cost/

#include <string.h>

int maximumCostSubstring(char* s, char* chars, int* vals, int valsSize) {
    (void)valsSize;
    int val[26];
    for (int i = 0; i < 26; i++) val[i] = i + 1;
    for (int i = 0; chars[i]; i++) val[chars[i] - 'a'] = vals[i];
    int best = 0, cur = 0;
    for (int i = 0; s[i]; i++) {
        cur += val[s[i] - 'a'];
        if (cur < 0) cur = 0;
        if (cur > best) best = cur;
    }
    return best;
}
