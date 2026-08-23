// LeetCode 0857 - Minimum Cost to Hire K Workers
// https://leetcode.com/problems/minimum-cost-to-hire-k-workers/

/**
 * @param {number[]} quality
 * @param {number[]} wage
 * @param {number} k
 * @return {number}
 */
var mincostToHireWorkers = function(quality, wage, k) {
    const n = quality.length;
    const workers = [];
    for (let i = 0; i < n; i++) workers.push([wage[i] / quality[i], quality[i]]);
    workers.sort((a, b) => a[0] - b[0]);
    const heap = [];
    const push = (q) => {
        heap.push(q);
        let i = heap.length - 1;
        while (i > 0) {
            const p = (i - 1) >> 1;
            if (heap[i] <= heap[p]) break;
            [heap[i], heap[p]] = [heap[p], heap[i]];
            i = p;
        }
    };
    const pop = () => {
        const top = heap[0];
        const last = heap.pop();
        if (heap.length) {
            heap[0] = last;
            let i = 0;
            while (true) {
                let largest = i;
                const l = i * 2 + 1, r = i * 2 + 2;
                if (l < heap.length && heap[l] > heap[largest]) largest = l;
                if (r < heap.length && heap[r] > heap[largest]) largest = r;
                if (largest === i) break;
                [heap[i], heap[largest]] = [heap[largest], heap[i]];
                i = largest;
            }
        }
        return top;
    };
    let totalQ = 0, ans = Number.POSITIVE_INFINITY;
    for (const [ratio, q] of workers) {
        push(q);
        totalQ += q;
        if (heap.length > k) totalQ -= pop();
        if (heap.length === k) ans = Math.min(ans, totalQ * ratio);
    }
    return ans;
};
