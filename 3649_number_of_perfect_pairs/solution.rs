// LeetCode 3649 - Number of Perfect Pairs
// https://leetcode.com/problems/number-of-perfect-pairs/

impl Solution {
    pub fn perfect_pairs(nums: Vec<i32>) -> i64 {
        let n = nums.len();
        let mut abs_nums: Vec<i32> = nums.iter().map(|&x| x.abs()).collect();
        abs_nums.sort_unstable();
        let mut ans = 0i64;
        let mut j = 0;
        for i in 0..n {
            if j < i + 1 {
                j = i + 1;
            }
            while j < n && abs_nums[j] <= 2 * abs_nums[i] {
                j += 1;
            }
            ans += (j - i - 1) as i64;
        }
        ans
    }
}
