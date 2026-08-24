// LeetCode 3479 - Fruits Into Baskets III
// https://leetcode.com/problems/fruits-into-baskets-iii/

var numOfUnplacedFruits = function(fruits, baskets) {
    const n = baskets.length;
    let size = 1;
    while (size < n) size <<= 1;
    const tree = new Array(size * 2).fill(0);
    for (let i = 0; i < n; i++) tree[size + i] = baskets[i];
    for (let i = size - 1; i > 0; i--) tree[i] = Math.max(tree[i * 2], tree[i * 2 + 1]);
    const find = (node, nl, nr, need) => {
        if (tree[node] < need) return -1;
        if (nl === nr) return nl;
        const mid = Math.floor((nl + nr) / 2);
        const left = find(node * 2, nl, mid, need);
        if (left !== -1) return left;
        return find(node * 2 + 1, mid + 1, nr, need);
    };
    const update = (idx) => {
        let p = size + idx;
        tree[p] = -1;
        for (p >>= 1; p > 0; p >>= 1) tree[p] = Math.max(tree[p * 2], tree[p * 2 + 1]);
    };
    let unplaced = 0;
    for (const f of fruits) {
        const idx = find(1, 0, size - 1, f);
        if (idx === -1 || idx >= n) unplaced++;
        else update(idx);
    }
    return unplaced;
};
