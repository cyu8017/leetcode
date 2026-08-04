// LeetCode 1904 - The Number of Full Rounds You Have Played
// https://leetcode.com/problems/the-number-of-full-rounds-you-have-played/

/**
 * @param {string} loginTime
 * @param {string} logoutTime
 * @return {number}
 */
var numberOfRounds = function(loginTime, logoutTime) {
    const toMin = (t) => {
        const [h, m] = t.split(":").map(Number);
        return h * 60 + m;
    };
    let start = toMin(loginTime), end = toMin(logoutTime);
    if (end < start) end += 24 * 60;
    start = Math.floor((start + 14) / 15) * 15;
    end = Math.floor(end / 15) * 15;
    return Math.max(0, Math.floor((end - start) / 15));
};
