// LeetCode 3525 - Find X Value of Array II
// https://leetcode.com/problems/find-x-value-of-array-ii/

var resultArray = function(nums, k, queries) {
    const n = nums.length;
    const ans = new Array(queries.length);
    for (let qi = 0; qi < queries.length; qi++) {
        const idx = queries[qi][0], val = queries[qi][1], start = queries[qi][2], x = queries[qi][3];
        nums[idx] = val;
        let prod = 1, cnt = 0;
        for (let i = start; i < n; i++) {
            prod = prod * (nums[i] % k) % k;
            if (prod === x) cnt++;
        }
        ans[qi] = cnt;
    }
    return ans;
};
