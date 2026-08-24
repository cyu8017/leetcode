// LeetCode 2545 - Sort the Students by Their Kth Score
// https://leetcode.com/problems/sort-the-students-by-their-kth-score/

export function sortTheStudents(score: number[][], k: number): number[][] {
    score.sort((a, b) => b[k] - a[k]);
    return score;
}
