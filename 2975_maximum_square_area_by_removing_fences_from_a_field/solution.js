// LeetCode 2975 - Maximum Square Area by Removing Fences From a Field
// https://leetcode.com/problems/maximum-square-area-by-removing-fences-from-a-field/

function gaps(fences, bound) {
    const list = [1, ...fences, bound];
    list.sort((a, b) => a - b);
    const g = new Set();
    for (let i = 0; i < list.length; i++)
        for (let j = i + 1; j < list.length; j++)
            g.add(list[j] - list[i]);
    return g;
}
var maximizeSquareArea = function(m, n, hFences, vFences) {
    const mod = 1000000007;
    const hg = gaps(hFences, m);
    const vg = gaps(vFences, n);
    let best = -1;
    for (const g of hg) {
        if (vg.has(g) && g > best) best = g;
    }
    if (best < 0) return -1;
    return Number(BigInt(best) * BigInt(best) % BigInt(mod));
};
