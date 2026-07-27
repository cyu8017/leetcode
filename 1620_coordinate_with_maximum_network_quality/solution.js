// LeetCode 1620 - Coordinate With Maximum Network Quality
// https://leetcode.com/problems/coordinate-with-maximum-network-quality/

/**
 * @param {number[][]} towers
 * @param {number} radius
 * @return {number[]}
 */
var bestCoordinate = function(towers, radius) {
    let best = [0, 0], quality = -1;
    for (let x = 0; x <= 50; x++) {
        for (let y = 0; y <= 50; y++) {
            let q = 0;
            for (const [a, b, v] of towers) {
                const d = Math.hypot(x - a, y - b);
                if (d <= radius) q += Math.floor(v / (1 + d));
            }
            if (q > quality) {
                quality = q;
                best = [x, y];
            }
        }
    }
    return best;
};
