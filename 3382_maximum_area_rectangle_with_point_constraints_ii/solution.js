// LeetCode 3382 - Maximum Area Rectangle With Point Constraints II
// https://leetcode.com/problems/maximum-area-rectangle-with-point-constraints-ii/

function pack(x, y) {
    return (BigInt(x) << 32n) ^ BigInt(y >>> 0);
}
var maxRectangleArea = function(xCoord, yCoord) {
    const n = xCoord.length;
    const points = Array.from({length: n}, (_, i) => [xCoord[i], yCoord[i]]);
    const set = new Set();
    for (const p of points) set.add(pack(p[0], p[1]));
    let ans = -1;
    for (let i = 0; i < n; i++) {
        for (let j = i + 1; j < n; j++) {
            const x1 = points[i][0], y1 = points[i][1];
            const x2 = points[j][0], y2 = points[j][1];
            if (x1 === x2 || y1 === y2) continue;
            if (!set.has(pack(x1, y2)) || !set.has(pack(x2, y1))) continue;
            const minX = Math.min(x1, x2), maxX = Math.max(x1, x2);
            const minY = Math.min(y1, y2), maxY = Math.max(y1, y2);
            let ok = true;
            for (const p of points) {
                const x = p[0], y = p[1];
                if (x > minX && x < maxX && y > minY && y < maxY) { ok = false; break; }
                const onBorder = ((x === minX || x === maxX) && y >= minY && y <= maxY) ||
                        ((y === minY || y === maxY) && x >= minX && x <= maxX);
                if (onBorder) {
                    const isCorner = (x === minX || x === maxX) && (y === minY || y === maxY);
                    if (!isCorner) { ok = false; break; }
                }
            }
            if (ok) {
                const area = (maxX - minX) * (maxY - minY);
                if (area > ans) ans = area;
            }
        }
    }
    return ans;
};
