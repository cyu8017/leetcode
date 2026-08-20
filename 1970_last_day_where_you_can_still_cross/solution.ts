// LeetCode 1970 - Last Day Where You Can Still Cross
// https://leetcode.com/problems/last-day-where-you-can-still-cross/

function latestDayToCross(row: number, col: number, cells: number[][]): number {
    const can = (day: number): boolean => {
        const blocked = new Set<string>();
        for (let i = 0; i < day; i++) blocked.add(`${cells[i][0] - 1},${cells[i][1] - 1}`);
        const stack: number[][] = [];
        const seen = new Set<string>();
        for (let c = 0; c < col; c++) {
            if (!blocked.has(`0,${c}`)) {
                stack.push([0, c]);
                seen.add(`0,${c}`);
            }
        }
        while (stack.length) {
            const [r, c] = stack.pop()!;
            if (r === row - 1) return true;
            for (const [nr, nc] of [[r - 1, c], [r + 1, c], [r, c - 1], [r, c + 1]]) {
                const key = `${nr},${nc}`;
                if (nr >= 0 && nr < row && nc >= 0 && nc < col && !blocked.has(key) && !seen.has(key)) {
                    seen.add(key);
                    stack.push([nr, nc]);
                }
            }
        }
        return false;
    };
    let lo = 1, hi = cells.length, ans = 0;
    while (lo <= hi) {
        const mid = (lo + hi) >> 1;
        if (can(mid)) {
            ans = mid;
            lo = mid + 1;
        } else hi = mid - 1;
    }
    return ans;
}
