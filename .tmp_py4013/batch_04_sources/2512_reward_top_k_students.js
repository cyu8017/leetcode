// LeetCode 2512 - Reward Top K Students
// https://leetcode.com/problems/reward-top-k-students/

/**
 * @param {string[]} positive_feedback
 * @param {string[]} negative_feedback
 * @param {string[]} report
 * @param {number[]} student_id
 * @param {number} k
 * @return {number[]}
 */
var topStudents = function(positive_feedback, negative_feedback, report, student_id, k) {
    const pos = new Set(positive_feedback);
    const neg = new Set(negative_feedback);
    const arr = Array(report.length);
    for (let i = 0; i < report.length; i++) {
        let score = 0;
        for (const w of report[i].split(' ')) {
            if (!w) continue;
            if (pos.has(w)) score += 3;
            else if (neg.has(w)) score--;
        }
        arr[i] = [student_id[i], score];
    }
    arr.sort((a, b) => a[1] !== b[1] ? b[1] - a[1] : a[0] - b[0]);
    const ans = Array(k);
    for (let i = 0; i < k; i++) ans[i] = arr[i][0];
    return ans;
};
