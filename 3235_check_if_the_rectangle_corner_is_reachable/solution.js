// LeetCode 3235 - Check if the Rectangle Corner Is Reachable
// https://leetcode.com/problems/check-if-the-rectangle-corner-is-reachable/

var canReachCorner = function(xCorner, yCorner, circles) {
    const n = circles.length;
    const vis = new Array(n).fill(false);
    const inCircle = (x, y, cx, cy, r) => {
        const dx = x - cx, dy = y - cy;
        return dx * dx + dy * dy <= r * r;
    };
    const crossLeftTop = (cx, cy, r) => {
        const a = Math.abs(cx) <= r && cy >= 0 && cy <= yCorner;
        const b = Math.abs(cy - yCorner) <= r && cx >= 0 && cx <= xCorner;
        return a || b;
    };
    const crossRightBottom = (cx, cy, r) => {
        const a = Math.abs(cx - xCorner) <= r && cy >= 0 && cy <= yCorner;
        const b = Math.abs(cy) <= r && cx >= 0 && cx <= xCorner;
        return a || b;
    };
    const dfs = (i) => {
        const [x1, y1, r1] = circles[i];
        if (crossRightBottom(x1, y1, r1)) return true;
        vis[i] = true;
        for (let j = 0; j < n; j++) {
            if (vis[j]) continue;
            const [x2, y2, r2] = circles[j];
            if ((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2) > (r1 + r2) * (r1 + r2)) continue;
            if (x1 * r2 + x2 * r1 < (r1 + r2) * xCorner
                && y1 * r2 + y2 * r1 < (r1 + r2) * yCorner
                && dfs(j)) return true;
        }
        return false;
    };
    for (let i = 0; i < n; i++) {
        const [x, y, r] = circles[i];
        if (inCircle(0, 0, x, y, r) || inCircle(xCorner, yCorner, x, y, r)) return false;
        if (!vis[i] && crossLeftTop(x, y, r) && dfs(i)) return false;
    }
    return true;
};
