// LeetCode 2964 - Number of Divisible Triplet Sums
// https://leetcode.com/problems/number-of-divisible-triplet-sums/

#include <vector>
#include <unordered_map>

class Solution {
public:
    int divisibleTripletCount(std::vector<int>& nums, int d) {
        int n = (int)nums.size(), ans = 0;
        for (int i = 0; i < n; i++) {
            std::unordered_map<int, int> freq;
            for (int j = i + 1; j < n; j++) {
                int need = (d - (nums[i] + nums[j]) % d) % d;
                ans += freq[need];
                freq[nums[j] % d]++;
            }
        }
        return ans;
    }
};
