// LeetCode 3985 - Palindromic Subarray Sum
// https://leetcode.com/problems/palindromic-subarray-sum/

impl Solution {
    pub fn max_palindromic_subarray_sum(nums: Vec<i32>) -> i64 {
        let n = nums.len();
        let mut prefix = vec![0i64; n + 1];
        for i in 0..n {
            prefix[i + 1] = prefix[i] + nums[i] as i64;
        }
        let mut odd = vec![0i32; n];
        let mut left = 0i32;
        let mut right = -1i32;
        for i in 0..n {
            let mut radius = 1i32;
            if i as i32 <= right {
                let mirror = (left + right - i as i32) as usize;
                radius = odd[mirror];
                if right - i as i32 + 1 < radius {
                    radius = right - i as i32 + 1;
                }
            }
            while i as i32 - radius >= 0
                && i + (radius as usize) < n
                && nums[i - radius as usize] == nums[i + radius as usize]
            {
                radius += 1;
            }
            odd[i] = radius;
            if i as i32 + radius - 1 > right {
                left = i as i32 - radius + 1;
                right = i as i32 + radius - 1;
            }
        }
        let mut even = vec![0i32; n];
        left = 0;
        right = -1;
        for i in 0..n {
            let mut radius = 0i32;
            if i as i32 <= right {
                let mirror = (left + right - i as i32 + 1) as usize;
                radius = even[mirror];
                if right - i as i32 + 1 < radius {
                    radius = right - i as i32 + 1;
                }
            }
            while i as i32 - radius - 1 >= 0
                && i + (radius as usize) < n
                && nums[i - radius as usize - 1] == nums[i + radius as usize]
            {
                radius += 1;
            }
            even[i] = radius;
            if i as i32 + radius - 1 > right {
                left = i as i32 - radius;
                right = i as i32 + radius - 1;
            }
        }
        let mut answer = 0i64;
        for i in 0..n {
            let mut sum = prefix[i + odd[i] as usize] - prefix[i - odd[i] as usize + 1];
            if sum > answer {
                answer = sum;
            }
            if even[i] > 0 {
                sum = prefix[i + even[i] as usize] - prefix[i - even[i] as usize];
                if sum > answer {
                    answer = sum;
                }
            }
        }
        answer
    }
}
