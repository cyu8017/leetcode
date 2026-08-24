// LeetCode 4011 - Count Subarrays With Even Odd Ratio I
// https://leetcode.com/problems/count-subarrays-with-even-odd-ratio-i/

impl Solution {
    pub fn count_ratio_subarrays(nums: Vec<i32>, a: i32, b: i32) -> i32 {
        let n = nums.len();
        let mut ans = 0i64;
        for i in 0..n {
            let mut y = 0;
            for j in i..n {
                y += nums[j] % 2;
                let x = (j - i + 1) as i32 - y;
                if y > 0 && x as i64 * b as i64 <= y as i64 * a as i64 {
                    ans += 1;
                }
            }
        }
        ans as i32
    }
}
