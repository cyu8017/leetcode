// LeetCode 3731 - Find Missing Elements
// https://leetcode.com/problems/find-missing-elements/

export function findMissingElements(nums: any): any {
    let mn = 100, mx = 0;
    const s = new Set();
    for (const x of nums) {
        mn = Math.min(mn, x);
        mx = Math.max(mx, x);
        s.add(x);
    }
    const ans = [];
    for (let x = mn + 1; x < mx; x++) {
        if (!s.has(x)) ans.push(x);
    }
    return ans;
}
