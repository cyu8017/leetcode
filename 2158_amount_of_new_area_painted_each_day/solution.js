// LeetCode 2158 - Amount of New Area Painted Each Day
// https://leetcode.com/problems/amount-of-new-area-painted-each-day/

/**
 * @param {number[][]} paint
 * @return {number[]}
 */
var amountPainted = function(paint) {
    const ans = new Array(paint.length).fill(0);
    const line = new Array(50001).fill(0);
    for (let i = 0; i < paint.length; i++) {
        const start = paint[i][0], end = paint[i][1];
        let j = start;
        while (j < end) {
            if (line[j] === 0) {
                ans[i]++;
                line[j] = end;
                j++;
            } else {
                const next = line[j];
                line[j] = Math.max(end, next);
                j = next;
            }
        }
    }
    return ans;
};
