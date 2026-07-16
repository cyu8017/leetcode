// LeetCode 0052 - N-Queens II
// https://leetcode.com/problems/n-queens-ii/

export function totalNQueens(n: number): number {
    let count = 0;
    const cols = new Set<number>();
    const diag1 = new Set<number>();
    const diag2 = new Set<number>();

    function backtrack(row: number): void {
        if (row === n) {
            count += 1;
            return;
        }

        for (let col = 0; col < n; col++) {
            if (cols.has(col) || diag1.has(row + col) || diag2.has(row - col)) {
                continue;
            }

            cols.add(col);
            diag1.add(row + col);
            diag2.add(row - col);
            backtrack(row + 1);
            cols.delete(col);
            diag1.delete(row + col);
            diag2.delete(row - col);
        }
    }

    backtrack(0);
    return count;
}
