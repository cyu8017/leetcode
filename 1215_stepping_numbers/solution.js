// LeetCode 1215 - Stepping Numbers
// https://leetcode.com/problems/stepping-numbers/

/**
 * @param {number} low
 * @param {number} high
 * @return {number[]}
 */
var countSteppingNumbers = function(low, high) {
    const answer = low === 0 ? [0] : [];
    const q = [];
    for (let i = 1; i <= 9; i++) q.push(i);
    let qi = 0;
    while (qi < q.length) {
        const x = q[qi++];
        if (x > high) continue;
        if (x >= low) answer.push(x);
        const last = x % 10;
        if (last > 0) q.push(x * 10 + last - 1);
        if (last < 9) q.push(x * 10 + last + 1);
    }
    return answer.sort((a, b) => a - b);
};
