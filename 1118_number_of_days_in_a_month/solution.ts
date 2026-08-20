// LeetCode 1118 - Number of Days in a Month
// https://leetcode.com/problems/number-of-days-in-a-month/

function numberOfDays(year: number, month: number): number {
    return new Date(year, month, 0).getDate();
}
