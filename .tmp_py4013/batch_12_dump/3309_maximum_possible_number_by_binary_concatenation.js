// LeetCode 3309 - Maximum Possible Number by Binary Concatenation
// https://leetcode.com/problems/maximum-possible-number-by-binary-concatenation/

function toBin(x) {
    if (x === 0) return '0';
    let s = '';
    while (x > 0) {
        s = String(x & 1) + s;
        x >>= 1;
    }
    return s;
}
function perm(i, idx, bs, ans) {
    if (i === 3) {
        const s = bs[idx[0]] + bs[idx[1]] + bs[idx[2]];
        let v = 0;
        for (const c of s) v = v * 2 + (c.charCodeAt(0) - 48);
        if (v > ans[0]) ans[0] = v;
        return;
    }
    for (let j = i; j < 3; j++) {
        let t = idx[i]; idx[i] = idx[j]; idx[j] = t;
        perm(i + 1, idx, bs, ans);
        t = idx[i]; idx[i] = idx[j]; idx[j] = t;
    }
}
var maxGoodNumber = function(nums) {
    const bs = [toBin(nums[0]), toBin(nums[1]), toBin(nums[2])];
    const idx = [0, 1, 2];
    const ans = [0];
    perm(0, idx, bs, ans);
    return ans[0];
};
