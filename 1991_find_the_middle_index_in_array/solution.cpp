// LeetCode 1991 - Find the Middle Index in Array
#include <numeric>
#include <vector>

class Solution {
public:
    int findMiddleIndex(std::vector<int>& nums) {
        int total = std::accumulate(nums.begin(), nums.end(), 0);
        int left = 0;
        for (int i = 0; i < (int)nums.size(); i++) {
            if (left == total - left - nums[i]) return i;
            left += nums[i];
        }
        return -1;
    }
};
