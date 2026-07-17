// LeetCode 1764 - Form Array by Concatenating Subarrays of Another Array
// https://leetcode.com/problems/form-array-by-concatenating-subarrays-of-another-array/

#include <stdbool.h>

static bool matches(const int* nums, int start, const int* g, int m) {
    for (int t = 0; t < m; t++) {
        if (nums[start + t] != g[t]) {
            return false;
        }
    }
    return true;
}

static bool dfs(int** groups, int groupsSize, const int* groupsColSize,
                const int* nums, int numsSize, int i, int start) {
    if (i == groupsSize) {
        return start == numsSize;
    }
    const int* g = groups[i];
    int m = groupsColSize[i];
    for (int j = start; j <= numsSize - m; j++) {
        if (matches(nums, j, g, m) && dfs(groups, groupsSize, groupsColSize, nums, numsSize, i + 1, j + m)) {
            return true;
        }
    }
    return false;
}

bool canChoose(int** groups, int groupsSize, int* groupsColSize, int* nums, int numsSize) {
    return dfs(groups, groupsSize, groupsColSize, nums, numsSize, 0, 0);
}
