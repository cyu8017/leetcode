// LeetCode 1001 - Grid Illumination
// https://leetcode.com/problems/grid-illumination/

function gridIllumination(n: number, lamps: number[][], queries: number[][]): number[] {
    const rows = new Map<number, number>();
    const cols = new Map<number, number>();
    const diag1 = new Map<number, number>();
    const diag2 = new Map<number, number>();
    const lit = new Set<string>();
    const bump = (map: Map<number, number>, key: number, delta: number): void => {
        map.set(key, (map.get(key) || 0) + delta);
    };
    for (const [r, c] of lamps) {
        const key = `${r},${c}`;
        if (lit.has(key)) continue;
        lit.add(key);
        bump(rows, r, 1);
        bump(cols, c, 1);
        bump(diag1, r - c, 1);
        bump(diag2, r + c, 1);
    }
    const ans: number[] = [];
    for (const [r, c] of queries) {
        const on = (rows.get(r) || 0) || (cols.get(c) || 0) ||
            (diag1.get(r - c) || 0) || (diag2.get(r + c) || 0);
        ans.push(on ? 1 : 0);
        for (let i = r - 1; i <= r + 1; i++) {
            for (let j = c - 1; j <= c + 1; j++) {
                const key = `${i},${j}`;
                if (lit.has(key)) {
                    lit.delete(key);
                    bump(rows, i, -1);
                    bump(cols, j, -1);
                    bump(diag1, i - j, -1);
                    bump(diag2, i + j, -1);
                }
            }
        }
    }
    return ans;
}
