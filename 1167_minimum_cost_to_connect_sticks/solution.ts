// LeetCode 1167 - Minimum Cost to Connect Sticks
// https://leetcode.com/problems/minimum-cost-to-connect-sticks/

function connectSticks(sticks: number[]): number {
    if (sticks.length <= 1) return 0;
    const heap = [...sticks];
    const siftUp = (i) => {
        while (i > 0) {
            const p = (i - 1) >> 1;
            if (heap[p] <= heap[i]) break;
            [heap[p], heap[i]] = [heap[i], heap[p]];
            i = p;
        }
    };
    const siftDown = (i) => {
        while (true) {
            let smallest = i;
            const l = 2 * i + 1, r = 2 * i + 2;
            if (l < heap.length && heap[l] < heap[smallest]) smallest = l;
            if (r < heap.length && heap[r] < heap[smallest]) smallest = r;
            if (smallest === i) break;
            [heap[i], heap[smallest]] = [heap[smallest], heap[i]];
            i = smallest;
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
    let ans = 0;
    while (heap.length > 1) {
        const cost = pop() + pop();
        ans += cost;
        push(cost);
    }
    return ans;
}
