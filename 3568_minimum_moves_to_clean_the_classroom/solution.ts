// LeetCode 3568 - Minimum Moves to Clean the Classroom
// https://leetcode.com/problems/minimum-moves-to-clean-the-classroom/

export function minMoves(classroom: any, energy: any): any {
    const m = classroom.length, n = classroom[0].length;
    const d = Array.from({length: m}, () => new Array(n).fill(0));
    let x = 0, y = 0, cnt = 0;
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            const c = classroom[i][j];
            if (c === 'S') { x = i; y = j; }
            else if (c === 'L') d[i][j] = cnt++;
        }
    }
    if (cnt === 0) return 0;
    const vis = Array.from({length: m}, () =>
        Array.from({length: n}, () =>
            Array.from({length: energy + 1}, () => new Array(1 << cnt).fill(false))));
    let q = [[x, y, energy, (1 << cnt) - 1]];
    vis[x][y][energy][(1 << cnt) - 1] = true;
    const dirs = [-1, 0, 1, 0, -1];
    let ans = 0;
    while (q.length) {
        const t = q;
        q = [];
        for (const s of t) {
            const i = s[0], j = s[1], curEnergy = s[2], mask = s[3];
            if (mask === 0) return ans;
            if (curEnergy <= 0) continue;
            for (let k = 0; k < 4; k++) {
                const nx = i + dirs[k], ny = j + dirs[k + 1];
                if (nx >= 0 && nx < m && ny >= 0 && ny < n && classroom[nx][ny] !== 'X') {
                    const nxtEnergy = classroom[nx][ny] === 'R' ? energy : curEnergy - 1;
                    let nxtMask = mask;
                    if (classroom[nx][ny] === 'L') nxtMask &= ~(1 << d[nx][ny]);
                    if (!vis[nx][ny][nxtEnergy][nxtMask]) {
                        vis[nx][ny][nxtEnergy][nxtMask] = true;
                        q.push([nx, ny, nxtEnergy, nxtMask]);
                    }
                }
            }
        }
        ans++;
    }
    return -1;
}
