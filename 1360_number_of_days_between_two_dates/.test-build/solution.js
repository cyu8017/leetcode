"use strict";
// LeetCode 1360 - Number Of Days Between Two Dates
// https://leetcode.com/problems/number-of-days-between-two-dates/
function daysBetweenDates(date1, date2) {
    const toDays = (s) => Math.floor(Date.parse(s + "T00:00:00Z") / 86400000);
    return Math.abs(toDays(date1) - toDays(date2));
}
