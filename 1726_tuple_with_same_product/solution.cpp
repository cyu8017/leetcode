// LeetCode 1726 - Tuple with Same Product
// https://leetcode.com/problems/tuple-with-same-product/

#include <unordered_map>
#include <vector>

class Solution {
public:
    int tupleSameProduct(std::vector<int>& nums) {
        std::unordered_map<int, int> counts;
        int n = nums.size();
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                counts[nums[i] * nums[j]]++;
            }
        }
        long long result = 0;
        for (const auto& [product, count] : counts) {
            result += static_cast<long long>(count) * (count - 1) * 4;
        }
        return static_cast<int>(result);
    }
};
