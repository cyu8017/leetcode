// LeetCode 2545 - Sort the Students by Their Kth Score
// https://leetcode.com/problems/sort-the-students-by-their-kth-score/

/**
 * @param {number[][]} score
 * @param {number} k
 * @return {number[][]}
 */
var sortTheStudents = function(score, k) {
    score.sort((a, b) => b[k] - a[k]);
    return score;
};
