// LeetCode 1911 - Maximum Alternating Subsequence Sum
// https://leetcode.com/problems/maximum-alternating-subsequence-sum/

function maxAlternatingSum(nums: number[]): number {
    let even = 0, odd = 0;
    for (const x of nums) {
        const ne = Math.max(even, odd + x);
        const no = Math.max(odd, even - x);
        even = ne;
        odd = no;
    }
    return even;
}
