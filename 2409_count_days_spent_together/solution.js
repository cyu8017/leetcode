// LeetCode 2409 - Count Days Spent Together
// https://leetcode.com/problems/count-days-spent-together/

/**
 * @param {string} arriveAlice
 * @param {string} leaveAlice
 * @param {string} arriveBob
 * @param {string} leaveBob
 * @return {number}
 */
var countDaysTogether = function(arriveAlice, leaveAlice, arriveBob, leaveBob) {
    const DAYS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
    const toDay = (s) => {
        const m = (s.charCodeAt(0) - 48) * 10 + (s.charCodeAt(1) - 48);
        const d = (s.charCodeAt(3) - 48) * 10 + (s.charCodeAt(4) - 48);
        let res = d;
        for (let i = 0; i < m - 1; i++) res += DAYS[i];
        return res;
    };
    const a1 = toDay(arriveAlice), a2 = toDay(leaveAlice);
    const b1 = toDay(arriveBob), b2 = toDay(leaveBob);
    const start = Math.max(a1, b1);
    const end = Math.min(a2, b2);
    if (end < start) return 0;
    return end - start + 1;
};
