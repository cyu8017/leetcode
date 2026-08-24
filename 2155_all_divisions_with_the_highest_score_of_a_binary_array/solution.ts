// LeetCode 2155 - All Divisions With the Highest Score of a Binary Array
// https://leetcode.com/problems/all-divisions-with-the-highest-score-of-a-binary-array/

export function maxScoreIndices(nums: number[]): number[] {
    const n = nums.length;
    let total1 = 0;
    for (const x of nums) total1 += x;
    let best = total1, left0 = 0, right1 = total1;
    let ans = [0];
    for (let i = 0; i < n; i++) {
        if (nums[i] === 0) left0++;
        else right1--;
        const score = left0 + right1;
        if (score > best) { best = score; ans = [i + 1]; }
        else if (score === best) ans.push(i + 1);
    }
    return ans;
}
