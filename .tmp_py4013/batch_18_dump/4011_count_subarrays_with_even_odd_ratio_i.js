// LeetCode 4011 - Count Subarrays With Even Odd Ratio I
// https://leetcode.com/problems/count-subarrays-with-even-odd-ratio-i/
var countRatioSubarrays = function(nums, a, b) {
        let n = nums.length;
        let ans = 0;
        for (let i = 0; i < n; i++) {
            let y = 0;
            for (let j = i; j < n; j++) {
                y += nums[j] % 2;
                let x = j - i + 1 - y;
                if (y > 0 && x * b <= y * a) ans++;
            }
        }
        return ans;
    
};
