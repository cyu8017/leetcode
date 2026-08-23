// LeetCode 3819 - Rotate Non Negative Elements
// https://leetcode.com/problems/rotate-non-negative-elements/

#include <vector>

class Solution {
public:
    std::vector<int> rotateElements(std::vector<int>& nums, int k) {
        std::vector<int> t;
        for (int x : nums) if (x >= 0) t.push_back(x);
        int m = (int)t.size();
        if (m == 0) return nums;
        std::vector<int> d(m);
        for (int i = 0; i < m; i++) d[((i - k) % m + m) % m] = t[i];
        int j = 0;
        for (int i = 0; i < (int)nums.size(); i++) {
            if (nums[i] >= 0) nums[i] = d[j++];
        }
        return nums;
    }
};
