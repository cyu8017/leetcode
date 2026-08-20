// LeetCode 1981 - Minimize the Difference Between Target and Chosen Elements
// https://leetcode.com/problems/minimize-the-difference-between-target-and-chosen-elements/

function minimizeTheDifference(mat: number[][], target: number): number {
    let possible = new Set<number>([0]);
    for (const row of mat) {
        const uniq = [...new Set(row)];
        const nxt = new Set<number>();
        for (const s of possible) for (const x of uniq) nxt.add(s + x);
        const kept = new Set([...nxt].filter((v) => v <= target));
        const above = [...nxt].filter((v) => v > target);
        if (above.length) kept.add(Math.min(...above));
        possible = kept.size ? kept : new Set([Math.min(...nxt)]);
    }
    let best = Infinity;
    for (const v of possible) best = Math.min(best, Math.abs(v - target));
    return best;
}
