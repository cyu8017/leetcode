// LeetCode 0703 - Kth Largest Element in a Stream
// https://leetcode.com/problems/kth-largest-element-in-a-stream/

class KthLargest {
    /**
     * @param {number} k
     * @param {number[]} nums
     */
    constructor(k, nums) {
        this.k = k;
        this.heap = [];
        for (const num of nums) this.add(num);
    }

    /**
     * @param {number} val
     * @return {number}
     */
    add(val) {
        this.heap.push(val);
        this.heap.sort((a, b) => a - b);
        if (this.heap.length > this.k) this.heap.shift();
        return this.heap[0];
    }
}
