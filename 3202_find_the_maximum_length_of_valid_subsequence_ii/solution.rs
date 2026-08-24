// LeetCode 3202 - Find the Maximum Length of Valid Subsequence II
// https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-ii/

impl Solution {
    pub fn maximum_length(nums: Vec<i32>, k: i32) -> i32 {
        let k = k as usize;
        let mut f = vec![vec![0; k]; k];
        let mut ans = 0;
        for mut x in nums {
            x %= k as i32;
            let x = x as usize;
            for j in 0..k {
                let y = (j + k - x) % k;
                f[x][y] = f[y][x] + 1;
                ans = ans.max(f[x][y]);
            }
        }
        ans
    }
}
