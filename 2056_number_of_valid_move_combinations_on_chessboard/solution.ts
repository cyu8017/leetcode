// LeetCode 2056 - Number of Valid Move Combinations On Chessboard
// https://leetcode.com/problems/number-of-valid-move-combinations-on-chessboard/

export function countCombinations(pieces: string[], positions: number[][]): number {
    const dirs = {
        rook: [[1,0],[-1,0],[0,1],[0,-1]],
        bishop: [[1,1],[1,-1],[-1,1],[-1,-1]],
        queen: [[1,0],[-1,0],[0,1],[0,-1],[1,1],[1,-1],[-1,1],[-1,-1]],
    };
    const n = pieces.length;
    const allMoves = Array.from({length: n}, () => []);
    for (let i = 0; i < n; i++) {
        const ms = [{dr: 0, dc: 0, steps: 0}];
        const r = positions[i][0], c = positions[i][1];
        for (const d of dirs[pieces[i]]) {
            let nr = r + d[0], nc = c + d[1], step = 1;
            while (nr >= 1 && nr <= 8 && nc >= 1 && nc <= 8) {
                ms.push({dr: d[0], dc: d[1], steps: step});
                nr += d[0]; nc += d[1]; step++;
            }
        }
        allMoves[i] = ms;
    }
    const chosen = new Array(n);
    let ans = 0;
    const okCombo = (end) => {
        let maxT = 0;
        for (let i = 0; i <= end; i++) maxT = Math.max(maxT, chosen[i].steps);
        for (let t = 1; t <= maxT; t++) {
            const seen = new Set();
            for (let i = 0; i <= end; i++) {
                const m = chosen[i];
                let pr, pc;
                if (m.steps === 0) { pr = positions[i][0]; pc = positions[i][1]; }
                else {
                    const use = Math.min(t, m.steps);
                    pr = positions[i][0] + m.dr * use;
                    pc = positions[i][1] + m.dc * use;
                }
                const key = (BigInt(pr) << 32n) ^ (BigInt(pc) & 0xffffffffn);
                if (seen.has(key)) return false;
                seen.add(key);
            }
        }
        return true;
    };
    const dfs = (i) => {
        if (i === pieces.length) { ans++; return; }
        for (const m of allMoves[i]) {
            chosen[i] = m;
            if (okCombo(i)) dfs(i + 1);
        }
    };
    dfs(0);
    return ans;
}
