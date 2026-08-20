// LeetCode 1154 - Day of the Year
// https://leetcode.com/problems/day-of-the-year/

function dayOfYear(date: string): number {
    const [year, month, day] = date.split("-").map(Number);
    const leap = year % 4 === 0 && (year % 100 !== 0 || year % 400 === 0);
    const days = [31, leap ? 29 : 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
    let ans = day;
    for (let i = 0; i < month - 1; i++) ans += days[i];
    return ans;
}
