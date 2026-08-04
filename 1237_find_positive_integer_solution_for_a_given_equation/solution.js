// LeetCode 1237 - Find Positive Integer Solution for a Given Equation
// https://leetcode.com/problems/find-positive-integer-solution-for-a-given-equation/

/**
 * @param {function} customfunction
 * @param {number} z
 * @return {number[][]}
 */
var findSolution = function(customfunction, z) {
    const answer = [];
    let x = 1, y = 1000;
    while (x <= 1000 && y >= 1) {
        const value = customfunction.f(x, y);
        if (value === z) {
            answer.push([x, y]);
            x++;
            y--;
        } else if (value < z) {
            x++;
        } else {
            y--;
        }
    }
    return answer;
};
