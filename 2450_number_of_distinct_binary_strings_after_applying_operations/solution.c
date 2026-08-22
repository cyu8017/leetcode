// LeetCode 2450 - Number of Distinct Binary Strings After Applying Operations
// https://leetcode.com/problems/number-of-distinct-binary-strings-after-applying-operations/

#include <string.h>

int countDistinctStrings(char* s, int k) {
    const int mod = 1000000007;
    int n = (int)strlen(s);
    int ans = 1;
    for (int i = 0; i < n - k + 1; i++) {
        ans = (int)((long long)ans * 2 % mod);
    }
    return ans;
}
