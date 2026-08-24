// LeetCode 2240 - Number of Ways to Buy Pens and Pencils
// https://leetcode.com/problems/number-of-ways-to-buy-pens-and-pencils/

export function waysToBuyPensPencils(total: number, cost1: number, cost2: number): number {
    let ans = 0;
    for (let pens = 0; pens * cost1 <= total; pens++) {
        const remain = total - pens * cost1;
        ans += Math.floor(remain / cost2) + 1;
    }
    return ans;
}
