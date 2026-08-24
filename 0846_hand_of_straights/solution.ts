// LeetCode 0846 - Hand of Straights
// https://leetcode.com/problems/hand-of-straights/

export function isNStraightHand(hand: number[], groupSize: number): boolean {
    if (hand.length % groupSize !== 0) return false;
    const count = new Map();
    for (const x of hand) count.set(x, (count.get(x) || 0) + 1);
    const keys = [...count.keys()].sort((a, b) => a - b);
    for (const start of keys) {
        const need = count.get(start) || 0;
        if (need === 0) continue;
        for (let x = start; x < start + groupSize; x++) {
            const c = count.get(x) || 0;
            if (c < need) return false;
            count.set(x, c - need);
        }
    }
    return true;
}
