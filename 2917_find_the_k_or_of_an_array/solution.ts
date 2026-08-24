// LeetCode 2917 - Find the K-or of an Array
// https://leetcode.com/problems/find-the-k-or-of-an-array/

export function findKOr(nums: number[], k: number): number {
    let ans = 0;
    for (let b = 0; b < 31; b++) {
        let cnt = 0;
        for (const v of nums) if ((v & (1 << b)) !== 0) cnt++;
        if (cnt >= k) ans |= 1 << b;
    }
    return ans;
}
