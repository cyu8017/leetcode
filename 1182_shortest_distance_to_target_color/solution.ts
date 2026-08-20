// LeetCode 1182 - Shortest Distance to Target Color
// https://leetcode.com/problems/shortest-distance-to-target-color/

function shortestDistanceColor(colors: number[], queries: number[][]): number[] {
    const pos = new Map();
    for (let i = 0; i < colors.length; i++) {
        if (!pos.has(colors[i])) pos.set(colors[i], []);
        pos.get(colors[i]).push(i);
    }
    const bisectLeft = (arr, x) => {
        let lo = 0, hi = arr.length;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (arr[mid] < x) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    };
    return queries.map(([i, c]) => {
        if (!pos.has(c)) return -1;
        const arr = pos.get(c);
        const idx = bisectLeft(arr, i);
        let best = Infinity;
        if (idx < arr.length) best = Math.min(best, arr[idx] - i);
        if (idx) best = Math.min(best, i - arr[idx - 1]);
        return best === Infinity ? -1 : best;
    });
}
