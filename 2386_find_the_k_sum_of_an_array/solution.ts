// LeetCode 2386 - Find the K-Sum of an Array
// https://leetcode.com/problems/find-the-k-sum-of-an-array/

export function kSum(nums: number[], k: number): number {
    let total = 0;
    const n = nums.length;
    const absNums = Array(n);
    for (let i = 0; i < n; i++) {
        if (nums[i] >= 0) {
            total += nums[i];
            absNums[i] = nums[i];
        } else {
            absNums[i] = -nums[i];
        }
    }
    absNums.sort((a, b) => a - b);
    // max-heap of [sum, i]
    const h = [];
    const push = (item) => {
        h.push(item);
        let i = h.length - 1;
        while (i > 0) {
            const p = (i - 1) >> 1;
            if (h[p][0] >= h[i][0]) break;
            [h[p], h[i]] = [h[i], h[p]];
            i = p;
        }
    };
    const pop = () => {
        const top = h[0];
        const last = h.pop();
        if (h.length > 0) {
            h[0] = last;
            let i = 0;
            while (true) {
                let largest = i;
                const l = i * 2 + 1, r = i * 2 + 2;
                if (l < h.length && h[l][0] > h[largest][0]) largest = l;
                if (r < h.length && h[r][0] > h[largest][0]) largest = r;
                if (largest === i) break;
                [h[largest], h[i]] = [h[i], h[largest]];
                i = largest;
            }
        }
        return top;
    };
    push([total, 0]);
    for (let t = 0; t < k - 1; t++) {
        const cur = pop();
        const sum = cur[0];
        const i = cur[1];
        if (i >= absNums.length) continue;
        push([sum - absNums[i], i + 1]);
        if (i > 0) {
            push([sum - absNums[i] + absNums[i - 1], i + 1]);
        }
    }
    return h[0][0];
}
