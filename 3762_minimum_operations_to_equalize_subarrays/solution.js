// LeetCode 3762 - Minimum Operations To Equalize Subarrays
// https://leetcode.com/problems/minimum_operations_to_equalize_subarrays/

var minOperations = function(nums, k, queries) {
    class Node {
        constructor(o) {
            if (o) {
                this.left = o.left; this.right = o.right; this.count = o.count; this.sum = o.sum;
            } else {
                this.left = 0; this.right = 0; this.count = 0; this.sum = 0;
            }
        }
    }
    const n = nums.length;
    const quotient = new Array(n), remainder = new Array(n);
    let values = new Array(n);
    for (let i = 0; i < n; i++) {
        quotient[i] = Math.floor(nums[i] / k);
        remainder[i] = nums[i] % k;
        values[i] = quotient[i];
    }
    values.sort((a, b) => a - b);
    let vu = 1;
    for (let i = 1; i < n; i++) if (values[i] !== values[vu - 1]) values[vu++] = values[i];
    values = values.slice(0, vu);

    const nodes = [new Node()];
    const roots = new Array(n + 1).fill(0);
    const umax = values.length - 1;

    const lowerBound = (a, x) => {
        let lo = 0, hi = a.length;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (a[mid] < x) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    };

    const update = (previous, lo, hi, position, value) => {
        const current = nodes.length;
        nodes.push(new Node(nodes[previous]));
        nodes[current].count++;
        nodes[current].sum += value;
        if (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (position <= mid) nodes[current].left = update(nodes[previous].left, lo, mid, position, value);
            else nodes[current].right = update(nodes[previous].right, mid + 1, hi, position, value);
        }
        return current;
    };

    const kth = (rightRoot, leftRoot, lo, hi, rank) => {
        if (lo === hi) return lo;
        const leftCount = nodes[nodes[rightRoot].left].count - nodes[nodes[leftRoot].left].count;
        const mid = (lo + hi) >> 1;
        if (rank <= leftCount) return kth(nodes[rightRoot].left, nodes[leftRoot].left, lo, mid, rank);
        return kth(nodes[rightRoot].right, nodes[leftRoot].right, mid + 1, hi, rank - leftCount);
    };

    const prefixStats = (rightRoot, leftRoot, lo, hi, end) => {
        if (end < lo) return [0, 0];
        if (hi <= end) return [
            nodes[rightRoot].count - nodes[leftRoot].count,
            nodes[rightRoot].sum - nodes[leftRoot].sum
        ];
        const mid = (lo + hi) >> 1;
        const left = prefixStats(nodes[rightRoot].left, nodes[leftRoot].left, lo, mid, end);
        let count = left[0], sum = left[1];
        if (end > mid) {
            const right = prefixStats(nodes[rightRoot].right, nodes[leftRoot].right, mid + 1, hi, end);
            count += right[0];
            sum += right[1];
        }
        return [count, sum];
    };

    for (let i = 0; i < n; i++) {
        const position = lowerBound(values, quotient[i]);
        roots[i + 1] = update(roots[i], 0, umax, position, quotient[i]);
    }

    const logv = new Array(n + 1).fill(0);
    for (let i = 2; i <= n; i++) logv[i] = logv[i >> 1] + 1;
    const levels = logv[n] + 1;
    const minTable = new Array(levels);
    const maxTable = new Array(levels);
    minTable[0] = remainder.slice();
    maxTable[0] = remainder.slice();
    for (let level = 1; level < levels; level++) {
        const length = n - (1 << level) + 1;
        minTable[level] = new Array(length);
        maxTable[level] = new Array(length);
        const half = 1 << (level - 1);
        for (let i = 0; i < length; i++) {
            minTable[level][i] = Math.min(minTable[level - 1][i], minTable[level - 1][i + half]);
            maxTable[level][i] = Math.max(maxTable[level - 1][i], maxTable[level - 1][i + half]);
        }
    }

    const answer = new Array(queries.length);
    for (let qi = 0; qi < queries.length; qi++) {
        const left = queries[qi][0], right = queries[qi][1];
        const length = right - left + 1;
        const level = logv[length];
        const offset = right - (1 << level) + 1;
        const minR = Math.min(minTable[level][left], minTable[level][offset]);
        const maxR = Math.max(maxTable[level][left], maxTable[level][offset]);
        if (minR !== maxR) {
            answer[qi] = -1;
            continue;
        }
        const medianIndex = kth(roots[right + 1], roots[left], 0, umax, Math.floor((length + 1) / 2));
        const median = values[medianIndex];
        const stats = prefixStats(roots[right + 1], roots[left], 0, umax, medianIndex);
        const leftCount = stats[0];
        const leftSum = stats[1];
        const totalSum = nodes[roots[right + 1]].sum - nodes[roots[left]].sum;
        answer[qi] = median * leftCount - leftSum + (totalSum - leftSum) - median * (length - leftCount);
    }
    return answer;
};
