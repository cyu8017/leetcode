// LeetCode 2758 - Next Day
// https://leetcode.com/problems/next-day/

/**
 * @return {string}
 */
Date.prototype.nextDay = function() {
    const d = new Date(this.valueOf());
    d.setDate(d.getDate() + 1);
    const y = d.getFullYear();
    const m = String(d.getMonth() + 1).padStart(2, '0');
    const day = String(d.getDate()).padStart(2, '0');
    return `${y}-${m}-${day}`;
};
