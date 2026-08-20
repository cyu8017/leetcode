// LeetCode 1992 - Find All Groups of Farmland
// https://leetcode.com/problems/find-all-groups-of-farmland/

function findFarmland(land: number[][]): number[][] {
    const m = land.length, n = land[0].length;
    const ans = [];
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (land[i][j] === 1 && (i === 0 || land[i - 1][j] === 0) && (j === 0 || land[i][j - 1] === 0)) {
                let r = i, c = j;
                while (r + 1 < m && land[r + 1][j] === 1) r++;
                while (c + 1 < n && land[i][c + 1] === 1) c++;
                ans.push([i, j, r, c]);
            }
        }
    }
    return ans;
}
