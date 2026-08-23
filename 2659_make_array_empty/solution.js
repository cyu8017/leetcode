// LeetCode 2659 - Make Array Empty
// https://leetcode.com/problems/make-array-empty/

var countOperationsToEmptyArray = function(nums) {
    const n = nums.length;
    const idx = Array.from({ length: n }, (_, i) => i);
    idx.sort((a, b) => nums[a] - nums[b]);
    let ans = n;
    for (let i = 1; i < n; i++)
        if (idx[i] < idx[i - 1]) ans += n - i;
    return ans;
};
