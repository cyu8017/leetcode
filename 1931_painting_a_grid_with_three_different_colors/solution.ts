// LeetCode 1931 - Painting a Grid With Three Different Colors
// https://leetcode.com/problems/painting-a-grid-with-three-different-colors/

function colorTheGrid(m: number, n: number): number {
    const MOD = 1000000007;
    const validColumn = (mask: number): boolean => {
        let prev = -1, x = mask;
        for (let i = 0; i < m; i++) {
            const c = x % 3;
            if (c === prev) return false;
            prev = c;
            x = Math.floor(x / 3);
        }
        return true;
    };
    const getColors = (mask: number): number[] => {
        const cols: number[] = [];
        let x = mask;
        for (let i = 0; i < m; i++) {
            cols.push(x % 3);
            x = Math.floor(x / 3);
        }
        return cols;
    };
    const states: number[] = [];
    for (let s = 0; s < 3 ** m; s++) if (validColumn(s)) states.push(s);
    const compat = new Map<number, number[]>(states.map((s) => [s, []]));
    for (const a of states) {
        const ca = getColors(a);
        for (const b of states) {
            const cb = getColors(b);
            if (ca.every((x, i) => x !== cb[i])) compat.get(a)!.push(b);
        }
    }
    const memo = new Map<string, number>();
    const dp = (col: number, prev: number): number => {
        const key = `${col},${prev}`;
        if (memo.has(key)) return memo.get(key)!;
        if (col === n) return 1;
        let total = 0;
        const options = prev === -1 ? states : compat.get(prev)!;
        for (const cur of options) total = (total + dp(col + 1, cur)) % MOD;
        memo.set(key, total);
        return total;
    };
    return dp(0, -1);
}
