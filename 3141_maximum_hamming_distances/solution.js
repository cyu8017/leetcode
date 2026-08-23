// LeetCode 3141 - Maximum Hamming Distances
// https://leetcode.com/problems/maximum-hamming-distances/

/**
 * @param {number[]} nums
 * @param {number} m
 * @return {number[]}
 */
var maxHammingDistances = function(nums, m) {
    const dist = new Array(1 << m).fill(-1);
    let q = [];
    for (const x of nums) {
        dist[x] = 0;
        q.push(x);
    }
    for (let k = 1; q.length; k++) {
        const t = [];
        for (const x of q) {
            for (let i = 0; i < m; i++) {
                const y = x ^ (1 << i);
                if (dist[y] === -1) {
                    dist[y] = k;
                    t.push(y);
                }
            }
        }
        q = t;
    }
    const ans = nums.slice();
    for (let i = 0; i < ans.length; i++) {
        const x = ans[i];
        ans[i] = m - dist[x ^ ((1 << m) - 1)];
    }
    return ans;
};
