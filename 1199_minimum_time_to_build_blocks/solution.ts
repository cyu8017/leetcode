// LeetCode 1199 - Minimum Time to Build Blocks
// https://leetcode.com/problems/minimum-time-to-build-blocks/

function minBuildTime(blocks: number[], split: number): number {
    const heap = [...blocks];
    const siftDown = (i) => {
        while (true) {
            let s = i;
            const l = 2 * i + 1, r = 2 * i + 2;
            if (l < heap.length && heap[l] < heap[s]) s = l;
            if (r < heap.length && heap[r] < heap[s]) s = r;
            if (s === i) break;
            [heap[i], heap[s]] = [heap[s], heap[i]];
            i = s;
        }
    };
    const siftUp = (i) => {
        while (i > 0) {
            const p = (i - 1) >> 1;
            if (heap[p] <= heap[i]) break;
            [heap[p], heap[i]] = [heap[i], heap[p]];
            i = p;
        }
    };
    for (let i = (heap.length >> 1) - 1; i >= 0; i--) siftDown(i);
    const pop = () => {
        const top = heap[0];
        const last = heap.pop();
        if (heap.length) { heap[0] = last; siftDown(0); }
        return top;
    };
    const push = (v) => { heap.push(v); siftUp(heap.length - 1); };
    while (heap.length > 1) {
        pop();
        push(pop() + split);
    }
    return heap[0];
}
