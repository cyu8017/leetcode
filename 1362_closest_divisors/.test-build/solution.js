"use strict";
// LeetCode 1362 - Closest Divisors
// https://leetcode.com/problems/closest-divisors/
function closestDivisors(num) {
    let best = null;
    for (const x of [num + 1, num + 2]) {
        for (let a = Math.floor(Math.sqrt(x)); a >= 1; a--) {
            if (x % a === 0) {
                const pair = [a, x / a];
                if (!best || pair[1] - pair[0] < best[1] - best[0])
                    best = pair;
                break;
            }
        }
    }
    return best;
}
