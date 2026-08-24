// LeetCode 3209 - Number of Subarrays With AND Value of K
// https://leetcode.com/problems/number-of-subarrays-with-and-value-of-k/

export function countSubarrays(nums: any, k: any): any {
    let pre = new Map();
    let ans = 0;
    for (const x of nums) {
        const cur = new Map();
        for (const [key, val] of pre) {
            const nk = x & key;
            cur.set(nk, (cur.get(nk) || 0) + val);
        }
        cur.set(x, (cur.get(x) || 0) + 1);
        ans += cur.get(k) || 0;
        pre = cur;
    }
    return ans;
}
