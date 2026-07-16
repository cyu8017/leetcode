export function longestIncreasingPath(matrix: number[][]): number {
    if (!matrix.length) return 0;
    const rows = matrix.length;
    const cols = matrix[0].length;
    const memo = Array.from({ length: rows }, () => Array(cols).fill(0));
    const directions: [number, number][] = [[1, 0], [-1, 0], [0, 1], [0, -1]];
    function dfs(row: number, col: number): number {
        if (memo[row][col]) return memo[row][col];
        let best = 1;
        for (const [dr, dc] of directions) {
            const nr = row + dr;
            const nc = col + dc;
            if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && matrix[nr][nc] > matrix[row][col]) {
                best = Math.max(best, 1 + dfs(nr, nc));
            }
        }
        memo[row][col] = best;
        return best;
    }
    let answer = 0;
    for (let row = 0; row < rows; row += 1) {
        for (let col = 0; col < cols; col += 1) answer = Math.max(answer, dfs(row, col));
    }
    return answer;
}
