// LeetCode 2554 - Maximum Number of Integers to Choose From a Range I
// https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-i/

#include <unordered_set>
#include <vector>

class Solution {
public:
    int maxCount(std::vector<int>& banned, int n, int maxSum) {
        std::unordered_set<int> ban(banned.begin(), banned.end());
        int ans = 0, sum = 0;
        for (int i = 1; i <= n; ++i) {
            if (ban.count(i)) continue;
            if (sum + i > maxSum) break;
            sum += i;
            ans++;
        }
        return ans;
    }
};
