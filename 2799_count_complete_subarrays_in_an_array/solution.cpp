// LeetCode 2799 - Count Complete Subarrays in an Array
// https://leetcode.com/problems/count-complete-subarrays-in-an-array/

#include <unordered_set>
#include <vector>

class Solution {
public:
    int countCompleteSubarrays(std::vector<int>& nums) {
        std::unordered_set<int> uniq(nums.begin(), nums.end());
        int need = (int)uniq.size(), ans = 0, n = (int)nums.size();
        for (int i = 0; i < n; i++) {
            std::unordered_set<int> seen;
            for (int j = i; j < n; j++) {
                seen.insert(nums[j]);
                if ((int)seen.size() == need) {
                    ans += n - j;
                    break;
                }
            }
        }
        return ans;
    }
};
