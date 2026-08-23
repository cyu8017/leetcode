// LeetCode 3717 - Minimum Operations to Make the Array Beautiful
// https://leetcode.com/problems/minimum-operations-to-make-the-array-beautiful/

#include <algorithm>
#include <climits>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int minOperations(std::vector<int>& nums) {
        std::unordered_map<int, int> f{{nums[0], 0}};
        for (int i = 1; i < (int)nums.size(); i++) {
            int x = nums[i];
            std::unordered_map<int, int> g;
            for (auto& [pre, s] : f) {
                int cur = (x + pre - 1) / pre * pre;
                while (cur <= 100) {
                    int val = s + (cur - x);
                    auto it = g.find(cur);
                    if (it == g.end() || it->second > val) g[cur] = val;
                    cur += pre;
                }
            }
            f.swap(g);
        }
        int ans = INT_MAX;
        for (auto& [_, v] : f) ans = std::min(ans, v);
        return ans;
    }
};
