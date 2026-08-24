// LeetCode 2250 - Count Number of Rectangles Containing Each Point
// https://leetcode.com/problems/count-number-of-rectangles-containing-each-point/

/**
 * @param {number[][]} rectangles
 * @param {number[][]} points
 * @return {number[]}
 */
var countRectangles = function(rectangles, points) {
    const byH = Array.from({length: 101}, () => []);
    for (const r of rectangles) byH[r[1]].push(r[0]);
    for (let h = 1; h <= 100; h++) byH[h].sort((a, b) => a - b);
    const ans = new Array(points.length);
    for (let i = 0; i < points.length; i++) {
        const x = points[i][0], y = points[i][1];
        let cnt = 0;
        for (let h = y; h <= 100; h++) {
            const xs = byH[h];
            let lo = 0, hi = xs.length;
            while (lo < hi) {
                const mid = (lo + hi) >> 1;
                if (xs[mid] < x) lo = mid + 1;
                else hi = mid;
            }
            cnt += xs.length - lo;
        }
        ans[i] = cnt;
    }
    return ans;
};
