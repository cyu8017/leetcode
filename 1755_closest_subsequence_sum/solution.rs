// LeetCode 1755 - Closest Subsequence Sum
// https://leetcode.com/problems/closest-subsequence-sum/

impl Solution {
    pub fn min_abs_difference(nums: Vec<i32>, goal: i32) -> i32 {
        let n = nums.len();
        let goal = goal as i64;

        fn sums(arr: &[i32]) -> Vec<i64> {
            let mut vals: Vec<i64> = Vec::with_capacity(1 << arr.len());
            vals.push(0);
            for &x in arr {
                let size = vals.len();
                for i in 0..size {
                    let v = vals[i] + x as i64;
                    vals.push(v);
                }
            }
            vals.sort_unstable();
            vals
        }

        let a = sums(&nums[..n / 2]);
        let b = sums(&nums[n / 2..]);
        let mut best = i64::MAX;
        let mut j = b.len() - 1;
        for &x in &a {
            while j > 0 && (x + b[j] - goal).abs() >= (x + b[j - 1] - goal).abs() {
                j -= 1;
            }
            best = best.min((x + b[j] - goal).abs());
        }
        best as i32
    }
}
