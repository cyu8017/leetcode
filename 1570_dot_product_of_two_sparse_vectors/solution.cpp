// LeetCode 1570 - Dot Product of Two Sparse Vectors
// https://leetcode.com/problems/dot-product-of-two-sparse-vectors/

#include <unordered_map>
#include <vector>

class SparseVector {
public:
    std::unordered_map<int, int> values;

    SparseVector(std::vector<int>& nums) {
        for (int i = 0; i < static_cast<int>(nums.size()); ++i) {
            if (nums[i] != 0) {
                values[i] = nums[i];
            }
        }
    }

    int dotProduct(SparseVector& vec) {
        if (values.size() > vec.values.size()) {
            return vec.dotProduct(*this);
        }
        int sum = 0;
        for (const auto& [i, x] : values) {
            auto it = vec.values.find(i);
            if (it != vec.values.end()) {
                sum += x * it->second;
            }
        }
        return sum;
    }
};

class Solution {
public:
    int dotProduct(std::vector<int>& nums1, std::vector<int>& nums2) {
        SparseVector a(nums1);
        SparseVector b(nums2);
        return a.dotProduct(b);
    }
};
