// LeetCode 3685 - Subsequence Sum After Capping Elements
// https://leetcode.com/problems/subsequence-sum-after-capping-elements/

export function subsequenceSumAfterCapping(nums: any, k: any): any {
    const n = nums.length;
    const sorted = nums.slice().sort((a, b) => a - b);
    const ans = new Array(n);
    const reach = new Array(k + 1).fill(false);
    reach[0] = true;
    let idx = 0;
    for (let x = 1; x <= n; x++) {
        while (idx < n && sorted[idx] <= x) {
            const v = sorted[idx];
            for (let s = k; s >= v; s--) {
                if (reach[s - v]) reach[s] = true;
            }
            idx++;
        }
        const tmp = reach.slice();
        const rem = n - idx;
        for (let s = 0; s <= k; s++) {
            if (!reach[s]) continue;
            for (let t = 1; t <= rem && s + t * x <= k; t++) tmp[s + t * x] = true;
        }
        ans[x - 1] = tmp[k];
    }
    return ans;
}
