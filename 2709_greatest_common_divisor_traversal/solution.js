// LeetCode 2709 - Greatest Common Divisor Traversal
// https://leetcode.com/problems/greatest-common-divisor-traversal/

var canTraverseAllPairs = function(nums) {
    const n = nums.length;
    if (n === 1) return true;
    let mx = nums[0];
    for (const x of nums) if (x > mx) mx = x;
    const parent = Array.from({ length: mx + 1 }, (_, i) => i);
    const find = (x) => {
        if (parent[x] !== x) parent[x] = find(parent[x]);
        return parent[x];
    };
    const unite = (a, b) => {
        const ra = find(a), rb = find(b);
        if (ra !== rb) parent[ra] = rb;
    };
    const has = new Array(mx + 1).fill(false);
    for (const x of nums) {
        if (x === 1) return false;
        has[x] = true;
    }
    const sieve = new Array(mx + 1).fill(0);
    for (let i = 2; i <= mx; i++) {
        if (sieve[i] === 0) {
            for (let j = i; j <= mx; j += i) {
                if (sieve[j] === 0) sieve[j] = i;
                if (has[j]) unite(i, j);
            }
        }
    }
    const root = find(nums[0]);
    for (const x of nums) if (find(x) !== root) return false;
    return true;
};
