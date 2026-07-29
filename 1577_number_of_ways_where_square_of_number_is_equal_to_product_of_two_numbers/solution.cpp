// LeetCode 1577 - Number of Ways Where Square of Number Is Equal to Product of Two Numbers
// https://leetcode.com/problems/number-of-ways-where-square-of-number-is-equal-to-product-of-two-numbers/

#include <unordered_map>
#include <vector>

class Solution {
public:
    int numTriplets(std::vector<int>& nums1, std::vector<int>& nums2) {
        auto count = [](const std::vector<int>& a, const std::vector<int>& b) -> int {
            std::unordered_map<long long, int> squares;
            for (int x : a) {
                ++squares[1LL * x * x];
            }
            std::unordered_map<long long, int> products;
            for (int i = 0; i < static_cast<int>(b.size()); ++i) {
                for (int j = i + 1; j < static_cast<int>(b.size()); ++j) {
                    ++products[1LL * b[i] * b[j]];
                }
            }
            int total = 0;
            for (const auto& [value, cnt] : squares) {
                auto it = products.find(value);
                if (it != products.end()) {
                    total += cnt * it->second;
                }
            }
            return total;
        };
        return count(nums1, nums2) + count(nums2, nums1);
    }
};
