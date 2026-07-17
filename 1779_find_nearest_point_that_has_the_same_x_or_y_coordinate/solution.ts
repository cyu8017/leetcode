// LeetCode 1779 - Find Nearest Point That Has the Same X or Y Coordinate
// https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/

function nearestValidPoint(x: number, y: number, points: number[][]): number {
    let best = Infinity;
    let ans = -1;
    for (let i = 0; i < points.length; i++) {
        const px = points[i][0];
        const py = points[i][1];
        if (px !== x && py !== y) {
            continue;
        }
        const dist = Math.abs(px - x) + Math.abs(py - y);
        if (dist < best) {
            best = dist;
            ans = i;
        }
    }
    return ans;
}
