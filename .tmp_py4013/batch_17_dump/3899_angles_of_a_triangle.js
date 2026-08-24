// LeetCode 3899 - Angles Of A Triangle
// https://leetcode.com/problems/angles-of-a-triangle/

var internalAngles = function(sides) {
    sides = sides.slice().sort((a, b) => a - b);
    const a = sides[0], b = sides[1], c = sides[2];
    if (a + b <= c) return [];
    const PI = Math.acos(-1.0);
    const A = Math.acos((b * b + c * c - a * a) / (2.0 * b * c)) * 180.0 / PI;
    const B = Math.acos((a * a + c * c - b * b) / (2.0 * a * c)) * 180.0 / PI;
    const C = 180.0 - A - B;
    return [A, B, C];
};
