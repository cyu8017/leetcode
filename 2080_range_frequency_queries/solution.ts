// LeetCode 2080 - Range Frequency Queries
// https://leetcode.com/problems/range-frequency-queries/

export class RangeFreqQuery {
    constructor(arr: any) {
        this.pos = new Map();
        for (let i = 0; i < arr.length; i++) {
            if (!this.pos.has(arr[i])) this.pos.set(arr[i], []);
            this.pos.get(arr[i]).push(i);
        }
    }

    lower(p: any, x: any): any {
        let lo = 0, hi = p.length;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (p[mid] < x) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }

    upper(p: any, x: any): any {
        let lo = 0, hi = p.length;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (p[mid] <= x) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }

    query(left: any, right: any, value: any): any {
        const p = this.pos.get(value);
        if (!p) return 0;
        return this.upper(p, right) - this.lower(p, left);
    }
}
