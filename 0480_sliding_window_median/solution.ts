// LeetCode 0480 - Sliding Window Median
// https://leetcode.com/problems/sliding-window-median/

export class Solution {
    medianSlidingWindow(nums: number[], k: number): number[] {
        const window = [...nums.slice(0, k)].sort((a, b) => a - b);
        const result: number[] = [];

        const appendMedian = (): void => {
            if (k % 2) {
                result.push(window[Math.floor(k / 2)]);
            } else {
                result.push((window[k / 2 - 1] + window[k / 2]) / 2);
            }
        };

        const lowerBound = (arr: number[], target: number): number => {
            let left = 0;
            let right = arr.length;
            while (left < right) {
                const mid = Math.floor((left + right) / 2);
                if (arr[mid] < target) left = mid + 1;
                else right = mid;
            }
            return left;
        };

        const insertSorted = (arr: number[], value: number): void => {
            const index = lowerBound(arr, value);
            arr.splice(index, 0, value);
        };

        appendMedian();
        for (let index = k; index < nums.length; index += 1) {
            const outgoing = nums[index - k];
            const incoming = nums[index];
            window.splice(lowerBound(window, outgoing), 1);
            insertSorted(window, incoming);
            appendMedian();
        }
        return result;
    }
}
