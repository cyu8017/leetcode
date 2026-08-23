// LeetCode 2611 - Mice and Cheese
// https://leetcode.com/problems/mice-and-cheese/

#include <algorithm>
#include <vector>

class Solution {
public:
    int miceAndCheese(std::vector<int>& reward1, std::vector<int>& reward2, int k) {
        int n = (int)reward1.size();
        std::vector<int> diff(n);
        int ans = 0;
        for (int i = 0; i < n; ++i) {
            ans += reward2[i];
            diff[i] = reward1[i] - reward2[i];
        }
        std::sort(diff.begin(), diff.end(), std::greater<int>());
        for (int i = 0; i < k; ++i) ans += diff[i];
        return ans;
    }
};
