// LeetCode 2889 - Reshape Data: Pivot
// https://leetcode.com/problems/reshape-data-pivot/

export function pivotTable(weather: any[]): any[] {
    const months = [];
    const byMonth = new Map();
    for (const r of weather) {
        const city = Array.isArray(r) ? r[0] : r.city;
        const month = Array.isArray(r) ? r[1] : r.month;
        const temperature = Array.isArray(r) ? r[2] : r.temperature;
        if (!byMonth.has(month)) {
            byMonth.set(month, {});
            months.push(month);
        }
        byMonth.get(month)[city] = temperature;
    }
    return months.map((month) => ({ month, ...byMonth.get(month) }));
}
