// LeetCode 1942 - The Number of the Smallest Unoccupied Chair
// https://leetcode.com/problems/the-number-of-the-smallest-unoccupied-chair/

function smallestChair(times: number[][], targetFriend: number): number {
    const order = [...times.keys()].sort((a, b) => times[a][0] - times[b][0]);
    const free: number[] = [];
    let nextChair = 0;
    const leaving: number[][] = [];
    const push = (heap: any[], item: any, cmp: (a: any, b: any) => number): void => {
        heap.push(item);
        let i = heap.length - 1;
        while (i > 0) {
            const p = (i - 1) >> 1;
            if (cmp(heap[p], heap[i]) <= 0) break;
            [heap[p], heap[i]] = [heap[i], heap[p]];
            i = p;
        }
    };
    const pop = (heap: any[], cmp: (a: any, b: any) => number): any => {
        const top = heap[0];
        const last = heap.pop();
        if (!heap.length) return top;
        heap[0] = last;
        let i = 0;
        while (true) {
            let s = i;
            const l = 2 * i + 1, r = 2 * i + 2;
            if (l < heap.length && cmp(heap[l], heap[s]) < 0) s = l;
            if (r < heap.length && cmp(heap[r], heap[s]) < 0) s = r;
            if (s === i) break;
            [heap[s], heap[i]] = [heap[i], heap[s]];
            i = s;
        }
        return top;
    };
    const cmpNum = (a: number, b: number): number => a - b;
    const cmpLeave = (a: number[], b: number[]): number => a[0] - b[0];
    for (const i of order) {
        const [arr, leave] = times[i];
        while (leaving.length && leaving[0][0] <= arr) push(free, pop(leaving, cmpLeave)[1], cmpNum);
        let chair: number;
        if (free.length) chair = pop(free, cmpNum);
        else chair = nextChair++;
        if (i === targetFriend) return chair;
        push(leaving, [leave, chair], cmpLeave);
    }
    return -1;
}
