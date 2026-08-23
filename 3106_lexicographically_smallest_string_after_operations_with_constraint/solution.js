// LeetCode 3106 - Lexicographically Smallest String After Operations With Constraint
// https://leetcode.com/problems/lexicographically-smallest-string-after-operations-with-constraint/

/**
 * @param {string} s
 * @param {number} k
 * @return {string}
 */
var getSmallestString = function(s, k) {
    const arr = s.split('');
    for (let i = 0; i < arr.length; i++) {
        const c1 = arr[i].charCodeAt(0);
        for (let c2 = 97; c2 < c1; c2++) {
            const d = Math.min(c1 - c2, 26 - (c1 - c2));
            if (d <= k) {
                arr[i] = String.fromCharCode(c2);
                k -= d;
                break;
            }
        }
    }
    return arr.join('');
};
