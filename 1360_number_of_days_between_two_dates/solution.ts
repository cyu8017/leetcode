// LeetCode 1360 - Number Of Days Between Two Dates
// https://leetcode.com/problems/number-of-days-between-two-dates/

function daysBetweenDates(date1: string, date2: string): number {
    const toDays = (s: any): any => Math.floor(Date.parse(s + "T00:00:00Z") / 86400000);
    return Math.abs(toDays(date1) - toDays(date2));
}
