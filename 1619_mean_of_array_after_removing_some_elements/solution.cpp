// LeetCode 1619 - Mean of Array After Removing Some Elements
// https://leetcode.com/problems/mean-of-array-after-removing-some-elements/

#include <algorithm>
#include <numeric>
#include <vector>

class Solution {
public:
    double trimMean(std::vector<int>& arr) {
        std::sort(arr.begin(), arr.end());
        const int k = static_cast<int>(arr.size()) / 20;
        const long long total = std::accumulate(arr.begin() + k, arr.end() - k, 0LL);
        return static_cast<double>(total) / (arr.size() - 2 * k);
    }
};
