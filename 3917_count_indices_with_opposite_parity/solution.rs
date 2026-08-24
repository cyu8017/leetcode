// LeetCode 3917 - Count Indices With Opposite Parity
// https://leetcode.com/problems/count-indices-with-opposite-parity/

impl Solution {
    pub fn count_opposite_parity(nums: Vec<i32>) -> Vec<i32> {
        let mut cnt = [0, 0];
        for &x in &nums {
            cnt[(x & 1) as usize] += 1;
        }
        let n = nums.len();
        let mut ans = vec![0; n];
        for i in 0..n {
            let x = nums[i];
            cnt[(x & 1) as usize] -= 1;
            ans[i] = cnt[((x & 1) ^ 1) as usize];
        }
        ans
    }
}
