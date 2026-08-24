// LeetCode 2933 - High-Access Employees
// https://leetcode.com/problems/high-access-employees/

export function findHighAccessEmployees(accessTimes: string[][]): string[] {
    const m = new Map();
    for (const [name, t] of accessTimes) {
        const hh = (t.charCodeAt(0) - 48) * 10 + (t.charCodeAt(1) - 48);
        const mm = (t.charCodeAt(2) - 48) * 10 + (t.charCodeAt(3) - 48);
        if (!m.has(name)) m.set(name, []);
        m.get(name).push(hh * 60 + mm);
    }
    const ans = [];
    for (const [name, times] of m) {
        times.sort((a, b) => a - b);
        for (let i = 0; i + 2 < times.length; i++) {
            if (times[i + 2] - times[i] < 60) {
                ans.push(name);
                break;
            }
        }
    }
    ans.sort();
    return ans;
}
