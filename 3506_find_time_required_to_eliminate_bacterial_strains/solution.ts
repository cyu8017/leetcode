// LeetCode 3506 - Find Time Required to Eliminate Bacterial Strains
// https://leetcode.com/problems/find-time-required-to-eliminate-bacterial-strains/

export function minEliminationTime(timeReq: any, splitTime: any): any {
    const pq = timeReq.slice().sort((a, b) => a - b);
    while (pq.length > 1) {
        pq.shift();
        const x = pq.shift();
        const v = x + splitTime;
        let lo = 0, hi = pq.length;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (pq[mid] < v) lo = mid + 1;
            else hi = mid;
        }
        pq.splice(lo, 0, v);
    }
    return pq[0];
}
