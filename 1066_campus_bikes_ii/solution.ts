// LeetCode 1066 - Campus Bikes II
// https://leetcode.com/problems/campus-bikes-ii/

function assignBikes(workers: number[][], bikes: number[][]): number {
    const m = bikes.length;
    const memo = new Map<string, number>();

    function dp(i: number, mask: number): number {
        if (i === workers.length) return 0;
        const key = i + "," + mask;
        if (memo.has(key)) return memo.get(key)!;
        let best = Infinity;
        const [wx, wy] = workers[i];
        for (let b = 0; b < m; b++) {
            if (mask & (1 << b)) continue;
            const [bx, by] = bikes[b];
            const dist = Math.abs(wx - bx) + Math.abs(wy - by);
            best = Math.min(best, dist + dp(i + 1, mask | (1 << b)));
        }
        memo.set(key, best);
        return best;
    }

    return dp(0, 0);
}
