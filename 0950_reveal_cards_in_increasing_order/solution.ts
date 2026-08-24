// LeetCode 0950 - Reveal Cards In Increasing Order
// https://leetcode.com/problems/reveal-cards-in-increasing-order/

export function deckRevealedIncreasing(deck: number[]): number[] {
    deck.sort((a, b) => a - b);
    const n = deck.length;
    const idx = [];
    for (let i = 0; i < n; i++) idx.push(i);
    const ans = new Array(n);
    for (const card of deck) {
        ans[idx.shift()] = card;
        if (idx.length) idx.push(idx.shift());
    }
    return ans;
}
