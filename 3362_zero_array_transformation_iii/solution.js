// LeetCode 3362 - Zero Array Transformation III
// https://leetcode.com/problems/zero-array-transformation-iii/

var maxRemoval = function(nums, queries) {
    queries.sort((a, b) => a[0] - b[0]);
    const h = [];
    const n = nums.length;
    const diff = new Array(n + 1).fill(0);
    let j = 0, used = 0, cur = 0;
    for (let i = 0; i < n; i++) {
        cur += diff[i];
        while (j < queries.length && queries[j][0] === i) {
            h.push(queries[j][1]);
            j++;
        }
        while (cur < nums[i]) {
            if (!h.length) return -1;
            h.sort((a, b) => b - a);
            if (h[0] < i) return -1;
            const r = h.shift();
            cur++;
            diff[r + 1]--;
            used++;
        }
    }
    return queries.length - used;
};
