// LeetCode 3458 - Select K Disjoint Special Substrings
// https://leetcode.com/problems/select-k-disjoint-special-substrings/

var maxSubstringLength = function(s, k) {
    const n = s.length;
    const first = new Array(26).fill(n), last = new Array(26).fill(-1);
    for (let i = 0; i < n; i++) {
        const ci = s.charCodeAt(i) - 97;
        if (first[ci] === n) first[ci] = i;
        last[ci] = i;
    }
    const segs = [];
    for (let c = 0; c < 26; c++) {
        if (last[c] === -1) continue;
        let l = first[c], r = last[c];
        for (let i = l; i <= r; i++) {
            const ci = s.charCodeAt(i) - 97;
            if (first[ci] < l) {
                l = first[ci];
                i = l - 1;
                continue;
            }
            if (last[ci] > r) r = last[ci];
        }
        if (!(l === 0 && r === n - 1)) segs.push([l, r]);
    }
    const uniq = new Set();
    const arr = [];
    for (const sg of segs) {
        const key = (BigInt(sg[0]) << 32n) | BigInt(sg[1] >>> 0);
        const ks = key.toString();
        if (!uniq.has(ks)) {
            uniq.add(ks);
            arr.push(sg);
        }
    }
    arr.sort((a, b) => a[1] - b[1]);
    let cnt = 0, end = -1;
    for (const sg of arr) {
        if (sg[0] > end) {
            cnt++;
            end = sg[1];
        }
    }
    return cnt >= k;
};
