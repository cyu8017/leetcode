// LeetCode 0786 - K-th Smallest Prime Fraction
// https://leetcode.com/problems/k-th-smallest-prime-fraction/

/**
 * @param {number[]} arr
 * @param {number} k
 * @return {number[]}
 */
var kthSmallestPrimeFraction = function(arr, k) {
    const n = arr.length;
    const heap = [];
    const push = (i, j) => {
        heap.push([i, j]);
        let idx = heap.length - 1;
        while (idx > 0) {
            const p = (idx - 1) >> 1;
            if (arr[heap[idx][0]] / arr[heap[idx][1]] >= arr[heap[p][0]] / arr[heap[p][1]]) break;
            [heap[idx], heap[p]] = [heap[p], heap[idx]];
            idx = p;
        }
    };
    const pop = () => {
        const top = heap[0];
        const last = heap.pop();
        if (heap.length) {
            heap[0] = last;
            let idx = 0;
            while (true) {
                let smallest = idx;
                const l = idx * 2 + 1, r = idx * 2 + 2;
                if (l < heap.length && arr[heap[l][0]] / arr[heap[l][1]] < arr[heap[smallest][0]] / arr[heap[smallest][1]]) smallest = l;
                if (r < heap.length && arr[heap[r][0]] / arr[heap[r][1]] < arr[heap[smallest][0]] / arr[heap[smallest][1]]) smallest = r;
                if (smallest === idx) break;
                [heap[idx], heap[smallest]] = [heap[smallest], heap[idx]];
                idx = smallest;
            }
        }
        return top;
    };
    for (let i = 0; i < n - 1; i++) push(i, n - 1);
    for (let t = 0; t < k - 1; t++) {
        const [i, j] = pop();
        if (j - 1 > i) push(i, j - 1);
    }
    const [i, j] = pop();
    return [arr[i], arr[j]];
};
