// LeetCode 3761 - Minimum Absolute Distance Between Mirror Pairs
// https://leetcode.com/problems/minimum-absolute-distance-between-mirror-pairs/

#include <algorithm>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int minMirrorPairDistance(std::vector<int>& nums) {
        int n = (int)nums.size();
        std::unordered_map<int, int> pos;
        int ans = n + 1;
        auto reverse = [](int x) {
            int y = 0;
            for (; x > 0; x /= 10) y = y * 10 + x % 10;
            return y;
        };
        for (int i = 0; i < n; i++) {
            auto it = pos.find(nums[i]);
            if (it != pos.end()) ans = std::min(ans, i - it->second);
            pos[reverse(nums[i])] = i;
        }
        return ans > n ? -1 : ans;
    }
};
