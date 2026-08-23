// LeetCode 3781 - Maximum Score After Binary Swaps
// https://leetcode.com/problems/maximum-score-after-binary-swaps/

#include <cstdint>
#include <queue>
#include <string>
#include <vector>

class Solution {
public:
    long long maximumScore(std::vector<int>& nums, std::string s) {
        int64_t ans = 0;
        std::priority_queue<int> pq;
        for (int i = 0; i < (int)nums.size(); i++) {
            pq.push(nums[i]);
            if (s[i] == '1') {
                ans += pq.top();
                pq.pop();
            }
        }
        return ans;
    }
};
