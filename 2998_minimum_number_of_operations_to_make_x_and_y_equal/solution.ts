// LeetCode 2998 - Minimum Number of Operations to Make X and Y Equal
// https://leetcode.com/problems/minimum-number-of-operations-to-make-x-and-y-equal/

export function minimumOperationsToMakeEqual(x: any, y: any): any {
    if (x <= y) return y - x;
    const q = [[x, 0]];
    const seen = new Set([x]);
    let qi = 0;
    while (qi < q.length) {
        const [v, d] = q[qi++];
        if (v === y) return d;
        const cands = [v + 1, v - 1, v % 11 === 0 ? (v / 11) | 0 : -1, v % 5 === 0 ? (v / 5) | 0 : -1];
        for (const nxt of cands) {
            if (nxt > 0 && nxt < 2 * x + 20 && !seen.has(nxt)) {
                seen.add(nxt);
                q.push([nxt, d + 1]);
            }
        }
    }
    return -1;
}
