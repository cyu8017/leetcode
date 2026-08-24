// LeetCode 3176 - Find the Maximum Length of a Good Subsequence I
// https://leetcode.com/problems/find-the-maximum-length-of-a-good-subsequence-i/

impl Solution {
    pub fn maximum_length(nums: Vec<i32>, k: i32) -> i32 {
        let n = nums.len();
        let k = k as usize;
        let mut f = vec![vec![0; k + 1]; n];
        let mut ans = 0;
        for i in 0..n {
            for h in 0..=k {
                for j in 0..i {
                    if nums[i] == nums[j] {
                        f[i][h] = f[i][h].max(f[j][h]);
                    } else if h > 0 {
                        f[i][h] = f[i][h].max(f[j][h - 1]);
                    }
                }
                f[i][h] += 1;
            }
            ans = ans.max(f[i][k]);
        }
        ans
    }
}
