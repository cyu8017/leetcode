// LeetCode 2126 - Destroying Asteroids
// https://leetcode.com/problems/destroying-asteroids/

/**
 * @param {number} mass
 * @param {number[]} asteroids
 * @return {boolean}
 */
var asteroidsDestroyed = function(mass, asteroids) {
    asteroids = asteroids.slice().sort((a, b) => a - b);
    let cur = mass;
    for (const a of asteroids) {
        if (cur < a) return false;
        cur += a;
    }
    return true;
};
