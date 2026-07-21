// LeetCode 1834 - Single-Threaded CPU
// https://leetcode.com/problems/single-threaded-cpu/

/**
 * @param {number[][]} tasks
 * @return {number[]}
 */
var getOrder = function(tasks) {
    const indexed = tasks.map((task, idx) => [idx, task]).sort((a, b) => a[1][0] - b[1][0] || a[0] - b[0]);
    let i = 0;
    const n = tasks.length;
    const heap = [];
    let time = 0;
    const order = [];

    const push = (item) => {
        heap.push(item);
        let idx = heap.length - 1;
        while (idx > 0) {
            const p = (idx - 1) >> 1;
            if (heap[p][0] < heap[idx][0] || (heap[p][0] === heap[idx][0] && heap[p][1] <= heap[idx][1])) break;
            [heap[p], heap[idx]] = [heap[idx], heap[p]];
            idx = p;
        }
    };
    const pop = () => {
        const top = heap[0];
        const last = heap.pop();
        if (heap.length === 0) return top;
        heap[0] = last;
        let idx = 0;
        const len = heap.length;
        while (true) {
            let s = idx;
            const l = 2 * idx + 1, r = 2 * idx + 2;
            const better = (a, b) => heap[a][0] < heap[b][0] || (heap[a][0] === heap[b][0] && heap[a][1] < heap[b][1]);
            if (l < len && better(l, s)) s = l;
            if (r < len && better(r, s)) s = r;
            if (s === idx) break;
            [heap[s], heap[idx]] = [heap[idx], heap[s]];
            idx = s;
        }
        return top;
    };

    while (i < n || heap.length) {
        if (i < n && heap.length === 0) time = Math.max(time, indexed[i][1][0]);
        while (i < n && indexed[i][1][0] <= time) {
            const [idx, task] = indexed[i];
            push([task[1], idx]);
            i += 1;
        }
        const [duration, idx] = pop();
        time += duration;
        order.push(idx);
    }
    return order;
};
