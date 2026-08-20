// LeetCode 1567 - Maximum Length of Subarray With Positive Product
// https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/
// @ts-nocheck

function getMaxLen(nums: number[]): number {
    let positive = 0, negative = 0, answer = 0;
    for (const x of nums) {
        if (x === 0) {
            positive = negative = 0;
        } else if (x > 0) {
            positive += 1;
            negative = negative ? negative + 1 : 0;
        } else {
            const np = negative ? negative + 1 : 0;
            negative = positive + 1;
            positive = np;
        }
        answer = Math.max(answer, positive);
    }
    return answer;
}
