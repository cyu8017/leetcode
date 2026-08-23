// LeetCode 2551 - Put Marbles in Bags
// https://leetcode.com/problems/put-marbles-in-bags/

#include <algorithm>
#include <vector>

class Solution {
public:
    long long putMarbles(std::vector<int>& weights, int k) {
        int n = (int)weights.size();
        if (k == 1 || k == n) return 0;
        std::vector<int> pair(n - 1);
        for (int i = 0; i < n - 1; ++i) pair[i] = weights[i] + weights[i + 1];
        std::sort(pair.begin(), pair.end());
        long long mn = 0, mx = 0;
        for (int i = 0; i < k - 1; ++i) {
            mn += pair[i];
            mx += pair[n - 2 - i];
        }
        return mx - mn;
    }
};
