// LeetCode 1646 - Get Maximum in Generated Array
// https://leetcode.com/problems/get-maximum-in-generated-array/

#include <algorithm>
#include <vector>

class Solution {
public:
    int getMaximumGenerated(int n) {
        if (n < 2) {
            return n;
        }
        std::vector<int> a(n + 1);
        a[1] = 1;
        for (int i = 2; i <= n; ++i) {
            a[i] = (i % 2 == 0) ? a[i / 2] : a[i / 2] + a[i / 2 + 1];
        }
        return *std::max_element(a.begin(), a.end());
    }
};
