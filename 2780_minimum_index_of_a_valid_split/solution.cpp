// LeetCode 2780 - Minimum Index of a Valid Split
// https://leetcode.com/problems/minimum-index-of-a-valid-split/

#include <unordered_map>
#include <vector>

class Solution {
public:
    int minimumIndex(std::vector<int>& nums) {
        std::unordered_map<int, int> freq;
        int dom = 0, best = 0;
        for (int v : nums) {
            if (++freq[v] > best) { best = freq[v]; dom = v; }
        }
        int left = 0, n = (int)nums.size();
        for (int i = 0; i < n - 1; i++) {
            if (nums[i] == dom) left++;
            int right = best - left;
            if (left * 2 > i + 1 && right * 2 > n - i - 1) return i;
        }
        return -1;
    }
};
