// LeetCode 1146 - Snapshot Array
// https://leetcode.com/problems/snapshot-array/

class SnapshotArray {
    snapId: any;
    data: any;

    constructor(length: number) {
        this.snapId = 0;
        this.data = Array.from({ length }, () => [[0, 0]]);
    }

    set(index: number, val: number): void {
        const hist = this.data[index];
        if (hist[hist.length - 1][0] === this.snapId) {
            hist[hist.length - 1][1] = val;
        } else {
            hist.push([this.snapId, val]);
        }
    }

    snap(): number {
        this.snapId++;
        return this.snapId - 1;
    }

    get(index: number, snap_id: number): number {
        const hist = this.data[index];
        let lo = 0, hi = hist.length - 1, ans = 0;
        while (lo <= hi) {
            const mid = (lo + hi) >> 1;
            if (hist[mid][0] <= snap_id) {
                ans = mid;
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return hist[ans][1];
    }
}
