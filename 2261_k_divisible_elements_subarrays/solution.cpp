// LeetCode 2261 - K Divisible Elements Subarrays
// https://leetcode.com/problems/k-divisible-elements-subarrays/

#include <vector>
#include <string>
#include <unordered_set>

class Solution {
public:
    int countDistinct(std::vector<int>& nums, int k, int p) {
        int n = (int)nums.size();
        std::unordered_set<std::string> seen;
        for (int i = 0; i < n; ++i) {
            int div = 0;
            std::string key;
            for (int j = i; j < n; ++j) {
                if (nums[j] % p == 0) div++;
                if (div > k) break;
                key += std::to_string(nums[j] + 1) + ",";
                seen.insert(key);
            }
        }
        return (int)seen.size();
    }
};
