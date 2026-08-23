// LeetCode 2659 - Make Array Empty
// https://leetcode.com/problems/make-array-empty/

#include <vector>
#include <algorithm>
#include <numeric>

class Solution {
public:
    long long countOperationsToEmptyArray(std::vector<int>& nums) {
        int n = (int)nums.size();
        std::vector<int> idx(n);
        std::iota(idx.begin(), idx.end(), 0);
        std::sort(idx.begin(), idx.end(), [&](int a, int b) { return nums[a] < nums[b]; });
        long long ans = n;
        for (int i = 1; i < n; i++)
            if (idx[i] < idx[i - 1]) ans += n - i;
        return ans;
    }
};
