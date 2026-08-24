// LeetCode 3371 - Identify the Largest Outlier in an Array
// https://leetcode.com/problems/identify-the-largest-outlier-in-an-array/

export function getLargestOutlier(nums: any): any {
    let sum = 0;
    const freq = new Map();
    for (const x of nums) {
        sum += x;
        freq.set(x, (freq.get(x) || 0) + 1);
    }
    let ans = -2147483648;
    for (const x of nums) {
        freq.set(x, freq.get(x) - 1);
        const rem = sum - x;
        if (rem % 2 === 0) {
            const cand = rem / 2;
            if ((freq.get(cand) || 0) > 0 && x > ans) ans = x;
        }
        freq.set(x, freq.get(x) + 1);
    }
    return ans;
}
