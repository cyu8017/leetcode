// LeetCode 2417 - Closest Fair Integer
// https://leetcode.com/problems/closest-fair-integer/

/**
 * @param {number} n
 * @return {number}
 */
var closestFair = function(n) {
    for (let x = n; ; x++) {
        const s = String(x);
        if (s.length % 2 !== 0) {
            let p = 1;
            for (let i = 0; i < s.length; i++) p *= 10;
            return closestFair(p);
        }
        let even = 0, odd = 0;
        for (const c of s) {
            if ((c.charCodeAt(0) - 48) % 2 === 0) even++;
            else odd++;
        }
        if (even === odd) return x;
    }
};
