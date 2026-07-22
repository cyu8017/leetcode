// LeetCode 1679 - Max Number of K-Sum Pairs
// https://leetcode.com/problems/max-number-of-k-sum-pairs/

#include <unordered_map>
#include <vector>

class Solution {
public:
    int maxOperations(std::vector<int>& nums, int k) {
        std::unordered_map<int, int> cnt;
        int ans = 0;
        for (int x : nums) {
            auto it = cnt.find(k - x);
            if (it != cnt.end() && it->second > 0) {
                --it->second;
                ++ans;
            } else {
                ++cnt[x];
            }
        }
        return ans;
    }
};
