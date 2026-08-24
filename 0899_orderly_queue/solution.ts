// LeetCode 0899 - Orderly Queue
// https://leetcode.com/problems/orderly-queue/

export function orderlyQueue(s: string, k: number): string {
    if (k > 1) return s.split("").sort().join("");
    let best = s;
    for (let i = 1; i < s.length; i++) {
        const cand = s.slice(i) + s.slice(0, i);
        if (cand < best) best = cand;
    }
    return best;
}
