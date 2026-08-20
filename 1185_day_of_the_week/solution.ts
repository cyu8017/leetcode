// LeetCode 1185 - Day of the Week
// https://leetcode.com/problems/day-of-the-week/

function dayOfTheWeek(day: number, month: number, year: number): string {
    const names = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
    return names[new Date(year, month - 1, day).getDay()];
}
