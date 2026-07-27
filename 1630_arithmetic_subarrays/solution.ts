// LeetCode 1630 - Arithmetic Subarrays
// https://leetcode.com/problems/arithmetic-subarrays/

function checkArithmeticSubarrays(nums: number[], l: number[], r: number[]): boolean[] {
    return l.map((a, idx) => {
        const x = nums.slice(a, r[idx] + 1).sort((p, q) => p - q);
        if (x.length < 3) return true;
        const d = x[1] - x[0];
        for (let i = 2; i < x.length; i++) if (x[i] - x[i - 1] !== d) return false;
        return true;
    });
}
