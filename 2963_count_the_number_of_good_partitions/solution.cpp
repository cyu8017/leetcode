// LeetCode 2963 - Count the Number of Good Partitions
// https://leetcode.com/problems/count-the-number-of-good-partitions/

#include <vector>
#include <unordered_map>

class Solution {
public:
    int numberOfGoodPartitions(std::vector<int>& nums) {
        const int mod = 1000000007;
        std::unordered_map<int, int> last;
        for (int i = 0; i < (int)nums.size(); i++) last[nums[i]] = i;
        int ans = 1, end = 0;
        for (int i = 0; i < (int)nums.size(); i++) {
            if (last[nums[i]] > end) end = last[nums[i]];
            if (i == end && i != (int)nums.size() - 1) ans = (int)(ans * 2LL % mod);
        }
        return ans;
    }
};
