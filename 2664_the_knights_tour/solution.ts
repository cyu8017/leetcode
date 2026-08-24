// LeetCode 2664 - The Knight's Tour
// https://leetcode.com/problems/the-knights-tour/

export function tourOfKnight(m: any, n: any, r: any, c: any): any {
    const DIRS = [[1,2],[1,-2],[-1,2],[-1,-2],[2,1],[2,-1],[-2,1],[-2,-1]];
    const ans = Array.from({ length: m }, () => new Array(n).fill(-1));
    const dfs = (x, y, step) => {
        ans[x][y] = step;
        if (step === m * n - 1) return true;
        for (const [dx, dy] of DIRS) {
            const nx = x + dx, ny = y + dy;
            if (nx >= 0 && nx < m && ny >= 0 && ny < n && ans[nx][ny] === -1)
                if (dfs(nx, ny, step + 1)) return true;
        }
        ans[x][y] = -1;
        return false;
    };
    dfs(r, c, 0);
    return ans;
}
