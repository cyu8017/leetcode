// LeetCode 2600 - K Items With the Maximum Sum
// https://leetcode.com/problems/k-items-with-the-maximum-sum/

export function kItemsWithMaximumSum(numOnes: number, numZeros: number, numNegOnes: number, k: number): number {
    let ans = 0;
    let take = Math.min(numOnes, k);
    ans += take;
    k -= take;
    take = Math.min(numZeros, k);
    k -= take;
    take = Math.min(numNegOnes, k);
    ans -= take;
    return ans;
}
