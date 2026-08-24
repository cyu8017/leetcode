// LeetCode 0632 - Smallest Range Covering Elements from K Lists
// https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/

export function smallestRange(nums: number[][]): number[] {
    const heap = [];
    const push = (item) => {
        heap.push(item);
        let i = heap.length - 1;
        while (i > 0) {
            const p = (i - 1) >> 1;
            if (heap[p][0] <= heap[i][0]) break;
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
                let smallest = i;
                const l = i * 2 + 1, r = i * 2 + 2;
                if (l < heap.length && heap[l][0] < heap[smallest][0]) smallest = l;
                if (r < heap.length && heap[r][0] < heap[smallest][0]) smallest = r;
                if (smallest === i) break;
                [heap[i], heap[smallest]] = [heap[smallest], heap[i]];
                i = smallest;
            }
        }
        return top;
    };
    let currentMax = -Infinity;
    for (let i = 0; i < nums.length; ++i) {
        const val = nums[i][0];
        push([val, i, 0]);
        currentMax = Math.max(currentMax, val);
    }
    let bestLeft = heap[0][0], bestRight = currentMax;
    while (true) {
        const [value, listIndex, index] = pop();
        if (currentMax - value < bestRight - bestLeft) {
            bestLeft = value;
            bestRight = currentMax;
        }
        if (index + 1 === nums[listIndex].length) break;
        const nxt = nums[listIndex][index + 1];
        push([nxt, listIndex, index + 1]);
        currentMax = Math.max(currentMax, nxt);
    }
    return [bestLeft, bestRight];
}
