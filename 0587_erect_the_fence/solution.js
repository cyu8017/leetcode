// LeetCode 0587 - Erect the Fence
// https://leetcode.com/problems/erect-the-fence/

/**
 * @param {number[][]} trees
 * @return {number[][]}
 */
var outerTrees = function(trees) {
    const points = trees.slice().sort((a, b) => a[0] !== b[0] ? a[0] - b[0] : a[1] - b[1]);
    if (points.length <= 1) return points;
    const cross = (o, a, b) => (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0]);
    const build = (ordered) => {
        const hull = [];
        for (const point of ordered) {
            while (hull.length >= 2 && cross(hull[hull.length - 2], hull[hull.length - 1], point) < 0) {
                hull.pop();
            }
            hull.push(point);
        }
        return hull;
    };
    const lower = build(points);
    const upper = build(points.slice().reverse());
    const seen = new Set();
    const unique = [];
    const addUnique = (point) => {
        const key = point[0] + "," + point[1];
        if (!seen.has(key)) {
            seen.add(key);
            unique.push(point);
        }
    };
    for (let i = 0; i + 1 < lower.length; ++i) addUnique(lower[i]);
    for (let i = 0; i + 1 < upper.length; ++i) addUnique(upper[i]);
    return unique;
};
