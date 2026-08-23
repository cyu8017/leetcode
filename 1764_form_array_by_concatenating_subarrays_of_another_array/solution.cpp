// LeetCode 1764 - Form Array by Concatenating Subarrays of Another Array
// https://leetcode.com/problems/form-array-by-concatenating-subarrays-of-another-array/

#include <vector>

class Solution {
public:
    bool canChoose(std::vector<std::vector<int>>& groups, std::vector<int>& nums) {
        return dfs(groups, nums, 0, 0);
    }

private:
    bool dfs(std::vector<std::vector<int>>& groups, std::vector<int>& nums, int i, int start) {
        int n = (int)nums.size();
        if (i == (int)groups.size()) {
            return start == n;
        }
        const std::vector<int>& g = groups[i];
        int m = (int)g.size();
        for (int j = start; j <= n - m; j++) {
            if (matches(nums, j, g) && dfs(groups, nums, i + 1, j + m)) {
                return true;
            }
        }
        return false;
    }

    bool matches(const std::vector<int>& nums, int start, const std::vector<int>& g) {
        for (int t = 0; t < (int)g.size(); t++) {
            if (nums[start + t] != g[t]) {
                return false;
            }
        }
        return true;
    }
};
