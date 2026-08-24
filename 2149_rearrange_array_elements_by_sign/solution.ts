// LeetCode 2149 - Rearrange Array Elements by Sign
// https://leetcode.com/problems/rearrange-array-elements-by-sign/

export function rearrangeArray(nums: number[]): number[] {
    const ans = new Array(nums.length);
    let pos = 0, neg = 1;
    for (const x of nums) {
        if (x > 0) { ans[pos] = x; pos += 2; }
        else { ans[neg] = x; neg += 2; }
    }
    return ans;
}
