// LeetCode 1515 - Best Position for a Service Centre
// https://leetcode.com/problems/best-position-for-a-service-centre/

/**
 * @param {number[][]} positions
 * @return {number}
 */
var getMinDistSum = function(positions) {
    let x = 0, y = 0;
    for (const [px, py] of positions) { x += px; y += py; }
    x /= positions.length;
    y /= positions.length;
    const hypot = (a, b) => Math.sqrt(a * a + b * b);
    const distance = (a, b) => {
        let s = 0;
        for (const [px, py] of positions) s += hypot(a - px, b - py);
        return s;
    };
    for (let iter = 0; iter < 10000; iter++) {
        let nxSum = 0, nySum = 0, den = 0;
        let coincident = null;
        for (const [px, py] of positions) {
            const d = hypot(x - px, y - py);
            if (d < 1e-12) { coincident = [px, py]; break; }
            nxSum += px / d;
            nySum += py / d;
            den += 1 / d;
        }
        const nx = coincident ? coincident[0] : nxSum / den;
        const ny = coincident ? coincident[1] : nySum / den;
        if (hypot(nx - x, ny - y) < 1e-8) { x = nx; y = ny; break; }
        x = nx; y = ny;
    }
    return distance(x, y);
};
