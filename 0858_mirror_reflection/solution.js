// LeetCode 0858 - Mirror Reflection
// https://leetcode.com/problems/mirror-reflection/

/**
 * @param {number} p
 * @param {number} q
 * @return {number}
 */
var mirrorReflection = function(p, q) {
    const gcd = (a, b) => {
        while (b !== 0) {
            const t = a % b;
            a = b;
            b = t;
        }
        return a;
    };
    const g = gcd(p, q);
    p /= g;
    q /= g;
    if (p % 2 === 0) return 2;
    if (q % 2 === 0) return 0;
    return 1;
};
