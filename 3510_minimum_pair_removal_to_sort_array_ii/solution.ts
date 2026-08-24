// LeetCode 3510 - Minimum Pair Removal to Sort Array II
// https://leetcode.com/problems/minimum-pair-removal-to-sort-array-ii/

export function minimumPairRemoval(nums: any): any {
    const n = nums.length;
    let inv = 0, ans = 0;
    const sl = [];
    const idx = new Set();
    for (let i = 0; i < n; i++) idx.add(i);
    const key = (sum, i) => sum * 1000000007 + i;
    const slMap = new Map();
    function addSl(sum: any, i: any): any {
        const k = key(sum, i);
        slMap.set(k, [sum, i]);
        let lo = 0, hi = sl.length;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (sl[mid][0] < sum || (sl[mid][0] === sum && sl[mid][1] < i)) lo = mid + 1;
            else hi = mid;
        }
        sl.splice(lo, 0, [sum, i]);
    }    function remSl(sum: any, i: any): any {
        const k = key(sum, i);
        if (!slMap.has(k)) return;
        slMap.delete(k);
        for (let t = 0; t < sl.length; t++) {
            if (sl[t][0] === sum && sl[t][1] === i) { sl.splice(t, 1); break; }
        }
    }    function ceiling(set: any, x: any): any {
        let best = null;
        for (const v of set) if (v >= x && (best === null || v < best)) best = v;
        return best;
    }    function floor(set: any, x: any): any {
        let best = null;
        for (const v of set) if (v <= x && (best === null || v > best)) best = v;
        return best;
    }    for (let i = 0; i < n - 1; i++) {
        if (nums[i] > nums[i + 1]) inv++;
        addSl(nums[i] + nums[i + 1], i);
    }
    while (inv > 0) {
        ans++;
        const p = sl.shift();
        slMap.delete(key(p[0], p[1]));
        const s = p[0], i = p[1];
        const j = ceiling(idx, i + 1);
        if (nums[i] > nums[j]) inv--;
        const h = floor(idx, i - 1);
        if (h !== null) {
            if (nums[h] > nums[i]) inv--;
            remSl(nums[h] + nums[i], h);
            if (nums[h] > s) inv++;
            addSl(nums[h] + s, h);
        }
        const kk = ceiling(idx, j + 1);
        if (kk !== null) {
            if (nums[j] > nums[kk]) inv--;
            remSl(nums[j] + nums[kk], j);
            if (s > nums[kk]) inv++;
            addSl(s + nums[kk], i);
        }
        nums[i] = s;
        idx.delete(j);
    }
    return ans;
}
