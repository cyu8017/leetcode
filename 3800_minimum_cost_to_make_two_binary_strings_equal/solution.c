// LeetCode 3800 - Minimum Cost To Make Two Binary Strings Equal
// https://leetcode.com/problems/minimum-cost-to-make-two-binary-strings-equal/

#include <string.h>

long long minimumCost(char* s, char* t, int flipCost, int swapCost, int crossCost) {
    long long diff[2] = {0, 0};
    int n = (int)strlen(s);
    for (int i = 0; i < n; i++) {
        if (s[i] != t[i]) diff[s[i] - '0']++;
    }
    long long ans = (diff[0] + diff[1]) * flipCost;
    long long mx = diff[0] > diff[1] ? diff[0] : diff[1];
    long long mn = diff[0] < diff[1] ? diff[0] : diff[1];
    long long cand = mn * swapCost + (mx - mn) * flipCost;
    if (cand < ans) ans = cand;
    long long avg = (mx + mn) / 2;
    cand = (avg - mn) * crossCost + avg * swapCost + (mx + mn - avg * 2) * flipCost;
    if (cand < ans) ans = cand;
    return ans;
}
