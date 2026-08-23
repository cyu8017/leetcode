// LeetCode 0493 - Reverse Pairs
// https://leetcode.com/problems/reverse-pairs/

class Solution {
    reversePairs(nums) {
        const mergeSort = (start, end) => {
            if (start >= end) return 0;
            const mid = Math.floor((start + end) / 2);
            let count = mergeSort(start, mid) + mergeSort(mid + 1, end);
            let j = mid + 1;
            for (let i = start; i <= mid; i += 1) {
                while (j <= end && nums[i] > 2 * nums[j]) j += 1;
                count += j - (mid + 1);
            }
            nums.splice(start, end - start + 1, ...nums.slice(start, end + 1).sort((a, b) => a - b));
            return count;
        };
        return mergeSort(0, nums.length - 1);
    }
}

module.exports = { Solution };
