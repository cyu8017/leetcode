// LeetCode 0939 - Minimum Area Rectangle
// https://leetcode.com/problems/minimum-area-rectangle/

export function minAreaRect(points: number[][]): number {
    const set = new Set(points.map(([x, y]) => x + "," + y));
    let ans = Infinity;
    for (let i = 0; i < points.length; i++) {
        for (let j = i + 1; j < points.length; j++) {
            const [x1, y1] = points[i];
            const [x2, y2] = points[j];
            if (x1 === x2 || y1 === y2) continue;
            if (set.has(x1 + "," + y2) && set.has(x2 + "," + y1)) {
                ans = Math.min(ans, Math.abs(x1 - x2) * Math.abs(y1 - y2));
            }
        }
    }
    return ans === Infinity ? 0 : ans;
}
