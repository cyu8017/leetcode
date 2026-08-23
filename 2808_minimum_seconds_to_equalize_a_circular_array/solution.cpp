// LeetCode 2808 - Minimum Seconds to Equalize a Circular Array
// https://leetcode.com/problems/minimum-seconds-to-equalize-a-circular-array/

#include <algorithm>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int minimumSeconds(std::vector<int>& nums) {
        int n = (int)nums.size();
        std::unordered_map<int, std::vector<int>> pos;
        for (int i = 0; i < n; i++) pos[nums[i]].push_back(i);
        int ans = n;
        for (auto& [_, p] : pos) {
            int maxGap = 0;
            for (int i = 0; i < (int)p.size(); i++) {
                int gap = (i + 1 < (int)p.size()) ? p[i + 1] - p[i] : p[0] + n - p[i];
                maxGap = std::max(maxGap, gap / 2);
            }
            ans = std::min(ans, maxGap);
        }
        return ans;
    }
};
