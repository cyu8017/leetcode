// LeetCode 1185 - Day of the Week
// https://leetcode.com/problems/day-of-the-week/

/**
 * @param {number} day
 * @param {number} month
 * @param {number} year
 * @return {string}
 */
var dayOfTheWeek = function(day, month, year) {
    const names = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
    return names[new Date(year, month - 1, day).getDay()];
};
