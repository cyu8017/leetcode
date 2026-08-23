// LeetCode 3119 - Maximum Number of Potholes That Can Be Fixed
// https://leetcode.com/problems/maximum-number-of-potholes-that-can-be-fixed/

#include <string>
#include <vector>
#include <algorithm>

class Solution {
public:
    int maxPotholes(std::string road, int budget) {
        road += '.';
        int n = (int)road.size();
        std::vector<int> cnt(n);
        int k = 0, ans = 0;
        for (char c : road) {
            if (c == 'x') k++;
            else if (k > 0) { cnt[k]++; k = 0; }
        }
        for (k = n - 1; k > 0 && budget > 0; k--) {
            int t = std::min(budget / (k + 1), cnt[k]);
            ans += t * k;
            budget -= t * (k + 1);
            cnt[k - 1] += cnt[k] - t;
        }
        return ans;
    }
};
