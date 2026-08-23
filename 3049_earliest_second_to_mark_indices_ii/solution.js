// LeetCode 3049 - Earliest Second to Mark Indices II
// https://leetcode.com/problems/earliest-second-to-mark-indices-ii/

function MinHeap(cmp) {
    this.a = [];
    this.cmp = cmp || ((x, y) => x - y);
}
MinHeap.prototype._up = function(i) {
    const a = this.a, cmp = this.cmp;
    while (i > 0) {
        const p = (i - 1) >> 1;
        if (cmp(a[i], a[p]) >= 0) break;
        [a[i], a[p]] = [a[p], a[i]];
        i = p;
    }
};
MinHeap.prototype._down = function(i) {
    const a = this.a, cmp = this.cmp, n = a.length;
    while (true) {
        let s = i, l = i * 2 + 1, r = l + 1;
        if (l < n && cmp(a[l], a[s]) < 0) s = l;
        if (r < n && cmp(a[r], a[s]) < 0) s = r;
        if (s === i) break;
        [a[i], a[s]] = [a[s], a[i]];
        i = s;
    }
};
MinHeap.prototype.push = function(x) { this.a.push(x); this._up(this.a.length - 1); };
MinHeap.prototype.pop = function() {
    const a = this.a;
    if (!a.length) return undefined;
    const top = a[0], last = a.pop();
    if (a.length) { a[0] = last; this._down(0); }
    return top;
};
MinHeap.prototype.peek = function() { return this.a[0]; };
MinHeap.prototype.size = function() { return this.a.length; };

/**
 * @param {number[]} nums
 * @param {number[]} changeIndices
 * @return {number}
 */
var earliestSecondToMarkIndices = function(nums, changeIndices) {
    const getSecondToIndex = (nums, changeIndices) => {
        const indexToFirstSecond = new Map();
        for (let second = 0; second < changeIndices.length; second++) {
            const index = changeIndices[second] - 1;
            if (nums[index] > 0 && !indexToFirstSecond.has(index))
                indexToFirstSecond.set(index, second);
        }
        const secondToIndex = new Map();
        for (const [idx, sec] of indexToFirstSecond) secondToIndex.set(sec, idx);
        return secondToIndex;
    };
    const canMark = (nums, secondToIndex, maxSecond, numsSum) => {
        const h = new MinHeap();
        let marks = 0;
        for (let second = maxSecond - 1; second >= 0; second--) {
            if (secondToIndex.has(second)) {
                h.push(nums[secondToIndex.get(second)]);
                if (marks === 0) {
                    h.pop();
                    marks++;
                } else {
                    marks--;
                }
            } else {
                marks++;
            }
        }
        const heapSize = h.size();
        let heapSum = 0;
        while (h.size()) heapSum += h.pop();
        const decrementAndMarkCost = numsSum - heapSum + (nums.length - heapSize);
        const zeroAndMarkCost = heapSize + heapSize;
        return decrementAndMarkCost + zeroAndMarkCost <= maxSecond;
    };
    const secondToIndex = getSecondToIndex(nums, changeIndices);
    let numsSum = 0;
    for (const v of nums) numsSum += v;
    let l = 0, r = changeIndices.length + 1;
    while (l < r) {
        const m = Math.floor((l + r) / 2);
        if (canMark(nums, secondToIndex, m, numsSum)) r = m;
        else l = m + 1;
    }
    return l <= changeIndices.length ? l : -1;
};
