// LeetCode 2948 - Make Lexicographically Smallest Array by Swapping Elements
// https://leetcode.com/problems/make-lexicographically-smallest-array-by-swapping-elements/

#include <algorithm>
#include <vector>

class Solution {
public:
    std::vector<int> lexicographicallySmallestArray(std::vector<int>& nums, int limit) {
        int n = (int)nums.size();
        std::vector<int> idx(n);
        for (int i = 0; i < n; i++) idx[i] = i;
        std::sort(idx.begin(), idx.end(), [&](int a, int b) { return nums[a] < nums[b]; });
        std::vector<int> ans(n);
        for (int i = 0; i < n; ) {
            int j = i + 1;
            while (j < n && nums[idx[j]] - nums[idx[j - 1]] <= limit) j++;
            std::vector<int> groupIdx(idx.begin() + i, idx.begin() + j);
            std::sort(groupIdx.begin(), groupIdx.end());
            for (int t = 0; t < j - i; t++) ans[groupIdx[t]] = nums[idx[i + t]];
            i = j;
        }
        return ans;
    }
};
