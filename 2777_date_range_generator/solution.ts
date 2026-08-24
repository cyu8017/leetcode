// LeetCode 2777 - Date Range Generator
// https://leetcode.com/problems/date-range-generator/

export function* dateRangeGenerator(start: string, end: string, step: number): Generator<string> {
    let cur = new Date(start + "T00:00:00");
    const last = new Date(end + "T00:00:00");
    while (cur <= last) {
        const y = cur.getFullYear();
        const m = String(cur.getMonth() + 1).padStart(2, "0");
        const d = String(cur.getDate()).padStart(2, "0");
        yield `${y}-${m}-${d}`;
        cur.setDate(cur.getDate() + step);
    }
}
