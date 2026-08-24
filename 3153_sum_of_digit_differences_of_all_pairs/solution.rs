// LeetCode 3153 - Sum of Digit Differences of All Pairs
// https://leetcode.com/problems/sum-of-digit-differences-of-all-pairs/

impl Solution {
    pub fn sum_digit_differences(mut nums: Vec<i32>) -> i64 {
        let n = nums.len();
        let m = ((nums[0] as f64).log10().floor() as i32) + 1;
        let mut ans = 0i64;
        for _ in 0..m {
            let mut cnt = [0i32; 10];
            for i in 0..n {
                cnt[(nums[i] % 10) as usize] += 1;
                nums[i] /= 10;
            }
            for v in cnt {
                ans += v as i64 * (n as i64 - v as i64);
            }
        }
        ans / 2
    }
}
