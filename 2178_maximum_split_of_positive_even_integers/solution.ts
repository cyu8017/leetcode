// LeetCode 2178 - Maximum Split of Positive Even Integers
// https://leetcode.com/problems/maximum-split-of-positive-even-integers/

export function maximumEvenSplit(finalSum: number): number[] {
    if (finalSum % 2 !== 0) return [];
    const ans = [];
    for (let x = 2; x <= finalSum; x += 2) {
        ans.push(x);
        finalSum -= x;
    }
    ans[ans.length - 1] += finalSum;
    return ans;
}
