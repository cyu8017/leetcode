// LeetCode 1998 - GCD Sort of an Array
// https://leetcode.com/problems/gcd-sort-of-an-array/

/**
 * @param {number[]} nums
 * @return {boolean}
 */
var gcdSort = function(nums) {
    const m = Math.max(...nums);
    const parent = Array.from({ length: m + 1 }, (_, i) => i);
    const find = (x) => {
        while (parent[x] !== x) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    };
    const union = (a, b) => {
        const ra = find(a), rb = find(b);
        if (ra !== rb) parent[rb] = ra;
    };
    const spf = Array.from({ length: m + 1 }, (_, i) => i);
    for (let i = 2; i * i <= m; i++) {
        if (spf[i] === i) {
            for (let j = i * i; j <= m; j += i) {
                if (spf[j] === j) spf[j] = i;
            }
        }
    }
    for (const x of new Set(nums)) {
        let y = x;
        while (y > 1) {
            const p = spf[y];
            union(x, p);
            while (y % p === 0) y = Math.floor(y / p);
        }
    }
    const sorted = nums.slice().sort((a, b) => a - b);
    for (let i = 0; i < nums.length; i++) {
        if (find(nums[i]) !== find(sorted[i])) return false;
    }
    return true;
};
