// LeetCode 0417 - Pacific Atlantic Water Flow
export function pacificAtlantic(heights: number[][]): number[][] {
    if (!heights.length || !heights[0].length) return [];
    const rows = heights.length;
    const cols = heights[0].length;

    const dfs = (row: number, col: number, visited: Set<string>, previous: number): void => {
        if (row < 0 || row >= rows || col < 0 || col >= cols) return;
        const key = `${row},${col}`;
        if (visited.has(key) || heights[row][col] < previous) return;
        visited.add(key);
        dfs(row + 1, col, visited, heights[row][col]);
        dfs(row - 1, col, visited, heights[row][col]);
        dfs(row, col + 1, visited, heights[row][col]);
        dfs(row, col - 1, visited, heights[row][col]);
    };

    const pacific = new Set<string>();
    const atlantic = new Set<string>();
    for (let row = 0; row < rows; row += 1) {
        dfs(row, 0, pacific, heights[row][0]);
        dfs(row, cols - 1, atlantic, heights[row][cols - 1]);
    }
    for (let col = 0; col < cols; col += 1) {
        dfs(0, col, pacific, heights[0][col]);
        dfs(rows - 1, col, atlantic, heights[rows - 1][col]);
    }

    const result: number[][] = [];
    for (const key of pacific) {
        if (atlantic.has(key)) {
            const [row, col] = key.split(",").map(Number);
            result.push([row, col]);
        }
    }
    return result;
}
