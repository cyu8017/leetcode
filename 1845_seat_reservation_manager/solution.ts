// LeetCode 1845 - Seat Reservation Manager
// https://leetcode.com/problems/seat-reservation-manager/

export class SeatManager {
    private readonly available: number[] = [];

    constructor(n: number) {
        for (let i = 1; i <= n; i++) this.available.push(i);
    }

    reserve(): number {
        const heap = this.available;
        const top = heap[0];
        const last = heap.pop()!;
        if (heap.length === 0) return top;
        heap[0] = last;
        let i = 0;
        const len = heap.length;
        while (true) {
            let s = i;
            const l = 2 * i + 1, r = 2 * i + 2;
            if (l < len && heap[l] < heap[s]) s = l;
            if (r < len && heap[r] < heap[s]) s = r;
            if (s === i) break;
            [heap[s], heap[i]] = [heap[i], heap[s]];
            i = s;
        }
        return top;
    }

    unreserve(seatNumber: number): null {
        const heap = this.available;
        heap.push(seatNumber);
        let i = heap.length - 1;
        while (i > 0) {
            const p = (i - 1) >> 1;
            if (heap[p] <= heap[i]) break;
            [heap[p], heap[i]] = [heap[i], heap[p]];
            i = p;
        }
        return null;
    }
}
