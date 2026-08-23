// LeetCode 0699 - Falling Squares
// https://leetcode.com/problems/falling-squares/

/**
 * @param {number[][]} positions
 * @return {number[]}
 */
var fallingSquares = function(positions) {
    const intervals = [];
    const answer = [];
    let maxHeight = 0;
    for (const pos of positions) {
        const left = pos[0], side = pos[1], right = left + side;
        let bas = 0;
        for (const it of intervals) {
            if (it[1] > left && it[0] < right) bas = Math.max(bas, it[2]);
        }
        const height = bas + side;
        intervals.push([left, right, height]);
        maxHeight = Math.max(maxHeight, height);
        answer.push(maxHeight);
    }
    return answer;
};
