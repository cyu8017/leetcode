// LeetCode 1722 - Minimize Hamming Distance After Swap Operations
// https://leetcode.com/problems/minimize-hamming-distance-after-swap-operations/

/**
 * @param {number[]} source
 * @param {number[]} target
 * @param {number[][]} allowedSwaps
 * @return {number}
 */
var minimumHammingDistance = function(source, target, allowedSwaps) {
    const n = source.length;
    const parent = Array.from({ length: n }, (_, i) => i);
    const find = (x) => {
        while (parent[x] !== x) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    };
    const union = (a, b) => {
        const ra = find(a);
        const rb = find(b);
        if (ra !== rb) {
            parent[rb] = ra;
        }
    };

    for (const [a, b] of allowedSwaps) {
        union(a, b);
    }
    const groups = new Map();
    for (let i = 0; i < n; i++) {
        const root = find(i);
        if (!groups.has(root)) {
            groups.set(root, new Map());
        }
        const counts = groups.get(root);
        counts.set(source[i], (counts.get(source[i]) || 0) + 1);
    }
    let ans = 0;
    for (let i = 0; i < n; i++) {
        const counts = groups.get(find(i));
        const remaining = counts.get(target[i]) || 0;
        if (remaining > 0) {
            counts.set(target[i], remaining - 1);
        } else {
            ans++;
        }
    }
    return ans;
};
