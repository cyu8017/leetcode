// LeetCode 2526 - Find Consecutive Integers from a Data Stream
// https://leetcode.com/problems/find-consecutive-integers-from-a-data-stream/

/**
 * @param {number} value
 * @param {number} k
 */
var DataStream = function(value, k) {
    this.value = value;
    this.k = k;
    this.streak = 0;
};

/** 
 * @param {number} num
 * @return {boolean}
 */
DataStream.prototype.consec = function(num) {
    if (num === this.value) this.streak++;
    else this.streak = 0;
    return this.streak >= this.k;
};
