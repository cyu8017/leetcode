// LeetCode 1828 - Queries on Number of Points Inside a Circle
// https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle/

/**
 * @param {number[][]} points
 * @param {number[][]} queries
 * @return {number[]}
 */
var countPoints = function(points, queries) {
    const result = [];
    for (const [xq, yq, r] of queries) {
        const radiusSq = r * r;
        let count = 0;
        for (const [x, y] of points) {
            if ((x - xq) * (x - xq) + (y - yq) * (y - yq) <= radiusSq) count += 1;
        }
        result.push(count);
    }
    return result;
};
