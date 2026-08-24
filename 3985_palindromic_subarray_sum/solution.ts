// LeetCode 3985 - Palindromic Subarray Sum
// https://leetcode.com/problems/palindromic-subarray-sum/

export function maxPalindromicSubarraySum(nums: any): any {
        let n = nums.length;
        let prefix = new Array(n + 1).fill(0);
        for (let i = 0; i < n; i++) prefix[i + 1] = prefix[i] + nums[i];
        let odd = new Array(n).fill(0);
        let left = 0, right = -1;
        for (let i = 0; i < n; i++) {
            let radius = 1;
            if (i <= right) {
                let mirror = left + right - i;
                radius = odd[mirror];
                if (right - i + 1 < radius) radius = right - i + 1;
            }
            while (i - radius >= 0 && i + radius < n && nums[i - radius] == nums[i + radius]) radius++;
            odd[i] = radius;
            if (i + radius - 1 > right) {
                left = i - radius + 1;
                right = i + radius - 1;
            }
        }
        let even = new Array(n).fill(0);
        left = 0; right = -1;
        for (let i = 0; i < n; i++) {
            let radius = 0;
            if (i <= right) {
                let mirror = left + right - i + 1;
                radius = even[mirror];
                if (right - i + 1 < radius) radius = right - i + 1;
            }
            while (i - radius - 1 >= 0 && i + radius < n && nums[i - radius - 1] == nums[i + radius]) radius++;
            even[i] = radius;
            if (i + radius - 1 > right) {
                left = i - radius;
                right = i + radius - 1;
            }
        }
        let answer = 0;
        for (let i = 0; i < n; i++) {
            let sum = prefix[i + odd[i]] - prefix[i - odd[i] + 1];
            if (sum > answer) answer = sum;
            if (even[i] > 0) {
                sum = prefix[i + even[i]] - prefix[i - even[i]];
                if (sum > answer) answer = sum;
            }
        }
        return answer;
    
}
