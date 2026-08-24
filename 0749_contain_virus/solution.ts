// LeetCode 0749 - Contain Virus
// https://leetcode.com/problems/contain-virus/

export function containVirus(isInfected: number[][]): number {
    const m = isInfected.length, n = isInfected[0].length;
    let walls = 0;
    const pack = (r, c) => (r * 1e6) + c;
    const unpack = (key) => [Math.floor(key / 1e6), key % 1e6];
    while (true) {
        const seen = new Set();
        const regions = [];
        const frontiers = [];
        const perimeters = [];
        for (let i = 0; i < m; i++) {
            for (let j = 0; j < n; j++) {
                const key = pack(i, j);
                if (isInfected[i][j] === 1 && !seen.has(key)) {
                    const stack = [[i, j]];
                    seen.add(key);
                    const region = new Set();
                    const frontier = new Set();
                    let perimeter = 0;
                    const dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]];
                    while (stack.length > 0) {
                        const [r, c] = stack.pop();
                        region.add(pack(r, c));
                        for (const d of dirs) {
                            const nr = r + d[0], nc = c + d[1];
                            if (nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
                            const nk = pack(nr, nc);
                            if (isInfected[nr][nc] === 1) {
                                if (!seen.has(nk)) {
                                    seen.add(nk);
                                    stack.push([nr, nc]);
                                }
                            } else if (isInfected[nr][nc] === 0) {
                                frontier.add(nk);
                                perimeter++;
                            }
                        }
                    }
                    regions.push(region);
                    frontiers.push(frontier);
                    perimeters.push(perimeter);
                }
            }
        }
        if (regions.length === 0) break;
        let quarantine = 0;
        for (let i = 1; i < regions.length; i++)
            if (frontiers[i].size > frontiers[quarantine].size) quarantine = i;
        if (frontiers[quarantine].size === 0) break;
        walls += perimeters[quarantine];
        for (const cell of regions[quarantine]) {
            const [r, c] = unpack(cell);
            isInfected[r][c] = -1;
        }
        for (let index = 0; index < frontiers.length; index++) {
            if (index === quarantine) continue;
            for (const cell of frontiers[index]) {
                const [r, c] = unpack(cell);
                isInfected[r][c] = 1;
            }
        }
    }
    return walls;
}
