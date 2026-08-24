// LeetCode 3047 - Find the Largest Area of Square Inside Two Rectangles
// https://leetcode.com/problems/find-the-largest-area-of-square-inside-two-rectangles/

var largestSquareArea = function(bottomLeft, topRight) {
    let ans = 0;
    const n = bottomLeft.length;
    for (let i = 0; i < n; i++) {
        const x1 = bottomLeft[i][0], y1 = bottomLeft[i][1];
        const x2 = topRight[i][0], y2 = topRight[i][1];
        for (let j = i + 1; j < n; j++) {
            const x3 = bottomLeft[j][0], y3 = bottomLeft[j][1];
            const x4 = topRight[j][0], y4 = topRight[j][1];
            const ww = Math.min(x2, x4) - Math.max(x1, x3);
            const h = Math.min(y2, y4) - Math.max(y1, y3);
            const e = Math.min(ww, h);
            if (e > 0) ans = Math.max(ans, e * e);
        }
    }
    return ans;
};
