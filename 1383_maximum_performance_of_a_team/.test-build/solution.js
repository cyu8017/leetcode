"use strict";
// LeetCode 1383: Maximum Performance Of A Team
function maxPerformance(n, speed, efficiency, k) {
    const engineers = speed.map((s, i) => [efficiency[i], s]).sort((a, b) => b[0] - a[0]);
    const heap = [];
    const push = (value) => { heap.push(value); let i = heap.length - 1; while (i) {
        const p = (i - 1) >> 1;
        if (heap[p] <= value)
            break;
        heap[i] = heap[p];
        i = p;
    } heap[i] = value; };
    const pop = () => { const result = heap[0], value = heap.pop(); if (heap.length) {
        let i = 0;
        while (i * 2 + 1 < heap.length) {
            let c = i * 2 + 1;
            if (c + 1 < heap.length && heap[c + 1] < heap[c])
                c++;
            if (heap[c] >= value)
                break;
            heap[i] = heap[c];
            i = c;
        }
        heap[i] = value;
    } return result; };
    let sum = 0n, best = 0n;
    for (const [e, s] of engineers) {
        push(s);
        sum += BigInt(s);
        if (heap.length > k)
            sum -= BigInt(pop());
        const performance = sum * BigInt(e);
        if (performance > best)
            best = performance;
    }
    return Number(best % 1000000007n);
}
