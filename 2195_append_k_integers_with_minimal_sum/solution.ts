// LeetCode 2195 - Append K Integers With Minimal Sum
// https://leetcode.com/problems/append-k-integers-with-minimal-sum/

export function minimalKSum(nums: number[], k: number): number {
    nums = nums.slice().sort((a, b) => a - b);
    let ans = 0;
    let prev = 0;
    for (const x of nums) {
        if (x <= prev) continue;
        let start = prev + 1, end = x - 1;
        if (start <= end) {
            let cnt = end - start + 1;
            if (cnt > k) { end = start + k - 1; cnt = k; }
            ans += (start + end) * cnt / 2;
            k -= cnt;
            if (k === 0) return ans;
        }
        prev = x;
    }
    const s = prev + 1, e = s + k - 1;
    ans += (s + e) * k / 2;
    return ans;
}
