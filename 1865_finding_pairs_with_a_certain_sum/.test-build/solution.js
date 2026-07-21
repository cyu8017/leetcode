"use strict";
// LeetCode 1865 - Finding Pairs With a Certain Sum
// https://leetcode.com/problems/finding-pairs-with-a-certain-sum/
Object.defineProperty(exports, "__esModule", { value: true });
exports.FindSumPairs = void 0;
class FindSumPairs {
    constructor(nums1, nums2) {
        this.nums1 = nums1;
        this.nums2 = nums2;
        this.counts = new Map();
        for (const num of nums2) {
            this.counts.set(num, (this.counts.get(num) || 0) + 1);
        }
    }
    add(index, val) {
        const old = this.nums2[index];
        this.counts.set(old, this.counts.get(old) - 1);
        this.nums2[index] += val;
        const neu = this.nums2[index];
        this.counts.set(neu, (this.counts.get(neu) || 0) + 1);
        return null;
    }
    count(tot) {
        let answer = 0;
        for (const num of this.nums1) {
            answer += this.counts.get(tot - num) || 0;
        }
        return answer;
    }
}
exports.FindSumPairs = FindSumPairs;
