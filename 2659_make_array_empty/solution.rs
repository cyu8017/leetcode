// LeetCode 2659 - Make Array Empty
// https://leetcode.com/problems/make-array-empty/

impl Solution {
    pub fn count_operations_to_empty_array(nums: Vec<i32>) -> i64 {
        let n = nums.len();
        let mut idx: Vec<usize> = (0..n).collect();
        idx.sort_by_key(|&i| nums[i]);
        let mut ans = n as i64;
        for i in 1..n {
            if idx[i] < idx[i - 1] {
                ans += (n - i) as i64;
            }
        }
        ans
    }
}
