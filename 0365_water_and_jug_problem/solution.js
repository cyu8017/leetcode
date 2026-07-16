// LeetCode 0365 - Water and Jug Problem
const gcd = (a, b) => (b === 0 ? a : gcd(b, a % b));

var canMeasureWater = function(x, y, target) {
    if (target === 0) return true;
    if (x + y < target) return false;
    return target % gcd(x, y) === 0;
};
