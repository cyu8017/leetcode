// LeetCode 1755 - Closest Subsequence Sum
// https://leetcode.com/problems/closest-subsequence-sum/

#include <algorithm>
#include <climits>
#include <cstdlib>
#include <vector>

class Solution {
public:
    int minAbsDifference(std::vector<int>& nums, int goal) {
        int n = static_cast<int>(nums.size());
        std::vector<int> left(nums.begin(), nums.begin() + n / 2);
        std::vector<int> right(nums.begin() + n / 2, nums.end());

        std::vector<long long> a = sums(left);
        std::vector<long long> b = sums(right);
        long long best = LLONG_MAX;
        size_t j = b.size() - 1;
        for (long long x : a) {
            while (j > 0 && std::llabs(x + b[j] - goal) >= std::llabs(x + b[j - 1] - goal)) {
                j--;
            }
            best = std::min(best, std::llabs(x + b[j] - goal));
        }
        return static_cast<int>(best);
    }

private:
    std::vector<long long> sums(const std::vector<int>& arr) {
        std::vector<long long> vals;
        vals.reserve(1ULL << arr.size());
        vals.push_back(0);
        for (int x : arr) {
            size_t size = vals.size();
            for (size_t i = 0; i < size; i++) {
                vals.push_back(vals[i] + x);
            }
        }
        std::sort(vals.begin(), vals.end());
        return vals;
    }
};
