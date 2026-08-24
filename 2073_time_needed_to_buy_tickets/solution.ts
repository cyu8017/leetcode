// LeetCode 2073 - Time Needed to Buy Tickets
// https://leetcode.com/problems/time-needed-to-buy-tickets/

export function timeRequiredToBuy(tickets: number[], k: number): number {
    let ans = 0;
    for (let i = 0; i < tickets.length; i++) {
        if (i <= k) ans += Math.min(tickets[i], tickets[k]);
        else ans += Math.min(tickets[i], tickets[k] - 1);
    }
    return ans;
}
