// LeetCode 0469 - Convex Polygon
// https://leetcode.com/problems/convex-polygon/

class Solution {
    isConvex(points) {
        let direction = 0;
        const count = points.length;
        for (let index = 0; index < count; index += 1) {
            const x1 = points[(index + 1) % count][0] - points[index][0];
            const y1 = points[(index + 1) % count][1] - points[index][1];
            const x2 = points[(index + 2) % count][0] - points[(index + 1) % count][0];
            const y2 = points[(index + 2) % count][1] - points[(index + 1) % count][1];
            const cross = x1 * y2 - y1 * x2;
            if (cross === 0) continue;
            const current = cross > 0 ? 1 : -1;
            if (direction === 0) direction = current;
            else if (direction !== current) return false;
        }
        return true;
    }
}

module.exports = { Solution };
