// LeetCode 3164 - Find the Number of Good Pairs II
// https://leetcode.com/problems/find-the-number-of-good-pairs-ii/

export function numberOfPairs(nums1: number[], nums2: number[], k: number): number {
    const cnt1 = new Map();
    for (const x of nums1) if (x % k === 0) cnt1.set(x / k, (cnt1.get(x / k) || 0) + 1);
    if (!cnt1.size) return 0;
    const cnt2 = new Map();
    for (const x of nums2) cnt2.set(x, (cnt2.get(x) || 0) + 1);
    let mx = 0;
    for (const x of cnt1.keys()) mx = Math.max(mx, x);
    let ans = 0;
    for (const [x, v] of cnt2) {
        let s = 0;
        for (let y = x; y <= mx; y += x) {
            const c = cnt1.get(y);
            if (c !== undefined) s += c;
        }
        ans += s * v;
    }
    return ans;
}
