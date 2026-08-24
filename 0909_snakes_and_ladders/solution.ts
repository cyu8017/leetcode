// LeetCode 0909 - Snakes and Ladders
// https://leetcode.com/problems/snakes-and-ladders/

export function snakesAndLadders(board: number[][]): number {
    const n = board.length;
    const target = n * n;
    const pos = (square) => {
        square--;
        const row = Math.floor(square / n);
        const rem = square % n;
        const r = n - 1 - row;
        const c = row % 2 === 0 ? rem : n - 1 - rem;
        return [r, c];
    };
    const q = [1];
    const seen = new Array(target + 1).fill(false);
    seen[1] = true;
    let moves = 0;
    while (q.length) {
        const sz = q.length;
        for (let s = 0; s < sz; s++) {
            const cur = q.shift();
            if (cur === target) return moves;
            const lim = Math.min(cur + 6, target);
            for (let nxt = cur + 1; nxt <= lim; nxt++) {
                const [r, c] = pos(nxt);
                const dest = board[r][c] !== -1 ? board[r][c] : nxt;
                if (!seen[dest]) {
                    seen[dest] = true;
                    q.push(dest);
                }
            }
        }
        moves++;
    }
    return -1;
}
