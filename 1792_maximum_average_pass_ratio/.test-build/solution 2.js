"use strict";
// LeetCode 1792 - Maximum Average Pass Ratio
// https://leetcode.com/problems/maximum-average-pass-ratio/
function maxAverageRatio(classes, extraStudents) {
    const gain = (p, t) => (p + 1) / (t + 1) - p / t;
    const heap = [];
    const siftDown = (i) => {
        const n = heap.length;
        while (true) {
            let largest = i;
            const l = 2 * i + 1;
            const r = 2 * i + 2;
            if (l < n && heap[l][0] > heap[largest][0])
                largest = l;
            if (r < n && heap[r][0] > heap[largest][0])
                largest = r;
            if (largest === i)
                break;
            [heap[largest], heap[i]] = [heap[i], heap[largest]];
            i = largest;
        }
    };
    for (const [p, t] of classes) {
        heap.push([gain(p, t), p, t]);
    }
    for (let i = (heap.length >> 1) - 1; i >= 0; i--)
        siftDown(i);
    for (let k = 0; k < extraStudents; k++) {
        const [, p, t] = heap[0];
        heap[0] = [gain(p + 1, t + 1), p + 1, t + 1];
        siftDown(0);
    }
    let total = 0;
    for (const [, p, t] of heap)
        total += p / t;
    return total / heap.length;
}
