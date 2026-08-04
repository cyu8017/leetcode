// LeetCode 1157 - Online Majority Element In Subarray
// https://leetcode.com/problems/online-majority-element-in-subarray/

/**
 * @param {number[]} arr
 */
var MajorityChecker = function(arr) {
    this.arr = arr;
    this.pos = new Map();
    for (let i = 0; i < arr.length; i++) {
        if (!this.pos.has(arr[i])) this.pos.set(arr[i], []);
        this.pos.get(arr[i]).push(i);
    }
};

/** 
 * @param {number} left 
 * @param {number} right 
 * @param {number} threshold
 * @return {number}
 */
MajorityChecker.prototype.query = function(left, right, threshold) {
    let candidate = 0, count = 0;
    for (let i = left; i <= right; i++) {
        if (count === 0) candidate = this.arr[i];
        count += this.arr[i] === candidate ? 1 : -1;
    }
    const locs = this.pos.get(candidate) || [];
    const bisectLeft = (arr, x) => {
        let lo = 0, hi = arr.length;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (arr[mid] < x) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    };
    const bisectRight = (arr, x) => {
        let lo = 0, hi = arr.length;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (arr[mid] <= x) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    };
    const freq = bisectRight(locs, right) - bisectLeft(locs, left);
    return freq >= threshold ? candidate : -1;
};
