// LeetCode 3572 - Maximize Y-Sum by Picking a Triplet of Distinct X-Values
// https://leetcode.com/problems/maximize-ysum-by-picking-a-triplet-of-distinct-xvalues/

#include <algorithm>
#include <unordered_set>
#include <vector>

class Solution {
public:
    int maxSumDistinctTriplet(std::vector<int>& x, std::vector<int>& y) {
        int n = (int)x.size();
        std::vector<std::pair<int, int>> arr(n);
        for (int i = 0; i < n; i++) arr[i] = {x[i], y[i]};
        std::sort(arr.begin(), arr.end(), [](auto& a, auto& b) { return a.second > b.second; });
        int ans = 0;
        std::unordered_set<int> vis;
        for (int i = 0; i < n; i++) {
            int a = arr[i].first, b = arr[i].second;
            if (!vis.count(a)) {
                vis.insert(a);
                ans += b;
                if ((int)vis.size() == 3) return ans;
            }
        }
        return -1;
    }
};
