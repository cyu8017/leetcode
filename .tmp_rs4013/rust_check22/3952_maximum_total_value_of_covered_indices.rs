struct Solution;
// LeetCode 3952 - Maximum Total Value of Covered Indices
// https://leetcode.com/problems/maximum-total-value-of-covered-indices/

impl Solution {
    pub fn max_total_value(nums: Vec<i32>, s: String) -> i32 {
        let bytes = s.as_bytes();
        let mut answer = 0;
        let mut i = 0;
        while i < bytes.len() {
            if bytes[i] == b'0' {
                i += 1;
                continue;
            }
            let start = i;
            while i < bytes.len() && bytes[i] == b'1' {
                i += 1;
            }
            let end = i - 1;
            if start == 0 {
                for index in start..=end {
                    answer += nums[index];
                }
                continue;
            }
            let mut minimum = nums[start - 1];
            let mut total = 0;
            for index in (start - 1)..=end {
                total += nums[index];
                if nums[index] < minimum {
                    minimum = nums[index];
                }
            }
            answer += total - minimum;
        }
        answer
    }
}

fn main() {}
