// LeetCode 1354 - Construct Target Array With Multiple Sums
// https://leetcode.com/problems/construct-target-array-with-multiple-sums/

/**
 * @param {number[]} target
 * @return {boolean}
 */
var isPossible = function(target) {
    if (target.length === 1) return target[0] === 1;
    const heap = [];
    const push = (x) => {
        heap.push(x);
        let i = heap.length - 1;
        while (i > 0) {
            const p = (i - 1) >> 1;
            if (heap[p] >= heap[i]) break;
            [heap[p], heap[i]] = [heap[i], heap[p]];
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
                let s = i;
                const l = 2 * i + 1, r = 2 * i + 2;
                if (l < heap.length && heap[l] > heap[s]) s = l;
                if (r < heap.length && heap[r] > heap[s]) s = r;
                if (s === i) break;
                [heap[i], heap[s]] = [heap[s], heap[i]];
                i = s;
            }
        }
        return top;
    };
    let total = 0;
    for (const x of target) {
        total += x;
        push(x);
    }
    while (true) {
        const x = pop();
        const rest = total - x;
        if (x === 1 || rest === 1) return true;
        if (rest === 0 || x <= rest) return false;
        const prev = x % rest;
        if (prev === 0) return false;
        total = rest + prev;
        push(prev);
    }
};
