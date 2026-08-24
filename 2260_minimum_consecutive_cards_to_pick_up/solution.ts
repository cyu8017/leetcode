// LeetCode 2260 - Minimum Consecutive Cards to Pick Up
// https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up/

export function minimumCardPickup(cards: number[]): number {
    const last = new Map();
    let ans = -1;
    for (let i = 0; i < cards.length; i++) {
        if (last.has(cards[i])) {
            const diff = i - last.get(cards[i]) + 1;
            if (ans === -1 || diff < ans) ans = diff;
        }
        last.set(cards[i], i);
    }
    return ans;
}
