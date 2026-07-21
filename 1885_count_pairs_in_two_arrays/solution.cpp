// LeetCode 1885 - Count Pairs in Two Arrays
// https://leetcode.com/problems/count-pairs-in-two-arrays/

#include <algorithm>
#include <vector>

class Solution {
public:
    long long countPairs(std::vector<int>& nums1, std::vector<int>& nums2) {
        int n = static_cast<int>(nums1.size());
        std::vector<int> diff(n);
        for (int i = 0; i < n; i++) {
            diff[i] = nums1[i] - nums2[i];
        }
        std::sort(diff.begin(), diff.end());
        long long answer = 0;
        for (int i = 0; i < n; i++) {
            int target = -diff[i];
            auto it = std::upper_bound(diff.begin() + i + 1, diff.end(), target);
            answer += diff.end() - it;
        }
        return answer;
    }
};
