// LeetCode 1654 - Minimum Jumps to Reach Home
// https://leetcode.com/problems/minimum-jumps-to-reach-home/

function minimumJumps(forbidden: number[], a: number, b: number, x: number): number {
    const bad = new Set(forbidden);
    const limit = Math.max(x, ...forbidden) + a + b;
    const q: [number, number, boolean][] = [[0, 0, false]];
    const seen = new Set(["0,0"]);
    while (q.length) {
        const [p, d, back] = q.shift()!;
        if (p === x) return d;
        for (const [np, nb] of [[p + a, false], [p - b, true]] as [number, boolean][]) {
            const key = `${np},${nb ? 1 : 0}`;
            if (np >= 0 && np <= limit && !bad.has(np) && !seen.has(key) && !(back && nb)) {
                seen.add(key);
                q.push([np, d + 1, nb]);
            }
        }
    }
    return -1;
}
