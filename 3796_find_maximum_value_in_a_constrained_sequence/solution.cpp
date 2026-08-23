// LeetCode 3796 - Find Maximum Value in a Constrained Sequence
// https://leetcode.com/problems/find-maximum-value-in-a-constrained-sequence/

#include <algorithm>
#include <climits>
#include <vector>

class Solution {
public:
    int maxValue(int n, std::vector<std::vector<int>>& restrictions, std::vector<int>& diff) {
        const int INF = INT_MAX / 4;
        std::vector<int> bound(n, INF);
        bound[0] = 0;
        for (auto& r : restrictions) bound[r[0]] = r[1];
        for (int i = 1; i < n; i++) bound[i] = std::min(bound[i], bound[i - 1] + diff[i - 1]);
        for (int i = n - 2; i >= 0; i--) bound[i] = std::min(bound[i], bound[i + 1] + diff[i]);
        return *std::max_element(bound.begin(), bound.end());
    }
};
