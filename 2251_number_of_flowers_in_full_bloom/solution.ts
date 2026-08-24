// LeetCode 2251 - Number of Flowers in Full Bloom
// https://leetcode.com/problems/number-of-flowers-in-full-bloom/

export function fullBloomFlowers(flowers: number[][], people: number[]): number[] {
    const start = [], end = [];
    for (const f of flowers) { start.push(f[0]); end.push(f[1]); }
    start.sort((a, b) => a - b);
    end.sort((a, b) => a - b);
    const upperBound = (a, t) => {
        let lo = 0, hi = a.length;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (a[mid] <= t) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    };
    const lowerBound = (a, t) => {
        let lo = 0, hi = a.length;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (a[mid] < t) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    };
    const ans = new Array(people.length);
    for (let i = 0; i < people.length; i++) {
        const t = people[i];
        ans[i] = upperBound(start, t) - lowerBound(end, t);
    }
    return ans;
}
