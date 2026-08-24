// LeetCode 2212 - Maximum Points in an Archery Competition
// https://leetcode.com/problems/maximum-points-in-an-archery-competition/

export function maximumBobPoints(numArrows: number, aliceArrows: number[]): number[] {
    let bestScore = -1;
    let best = new Array(12).fill(0);
    const bob = new Array(12).fill(0);
    function dfs(i: any, remain: any, score: any): any {
        if (i === 12) {
            if (score > bestScore) {
                bestScore = score;
                best = bob.slice();
                if (remain > 0) best[0] += remain;
            }
            return;
        }
        dfs(i + 1, remain, score);
        const need = aliceArrows[i] + 1;
        if (remain >= need) {
            bob[i] = need;
            dfs(i + 1, remain - need, score + i);
            bob[i] = 0;
        }
    }    dfs(0, numArrows, 0);
    return best;
}
