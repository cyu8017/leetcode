// LeetCode 3919 - Minimum Cost To Move Between Indices
// https://leetcode.com/problems/minimum-cost-to-move-between-indices/

var minCost = function(nums, queries) {
    const n = nums.length;
    const s1 = new Array(n).fill(0);
    const s2 = new Array(n).fill(0);
    for (let i = 1; i < n; i++) {
        let c1 = 1;
        if (i > 1 && nums[i - 1] - nums[i - 2] <= nums[i] - nums[i - 1]) c1 = nums[i] - nums[i - 1];
        let c2 = 1;
        if (i < n - 1 && nums[i] - nums[i - 1] > nums[i + 1] - nums[i]) c2 = nums[i] - nums[i - 1];
        s1[i] = s1[i - 1] + c1;
        s2[i] = s2[i - 1] + c2;
    }
    const ans = new Array(queries.length);
    for (let i = 0; i < queries.length; i++) {
        const l = queries[i][0], r = queries[i][1];
        ans[i] = (l < r) ? (s1[r] - s1[l]) : (s2[l] - s2[r]);
    }
    return ans;
};
