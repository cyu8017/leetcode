// LeetCode 1507 - Reformat Date
// https://leetcode.com/problems/reformat-date/
// @ts-nocheck

function reformatDate(date: string): string {
    const months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"];
    const [day, month, year] = date.split(" ");
    const m = String(months.indexOf(month) + 1).padStart(2, "0");
    const d = String(parseInt(day, 10)).padStart(2, "0");
    return `${year}-${m}-${d}`;
}
