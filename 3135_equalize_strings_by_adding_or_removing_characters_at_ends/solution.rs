// LeetCode 3135 - Equalize Strings by Adding or Removing Characters at Ends
// https://leetcode.com/problems/equalize-strings-by-adding-or-removing-characters-at-ends/

impl Solution {
    pub fn min_operations(initial: String, target: String) -> i32 {
        let a = initial.as_bytes();
        let b = target.as_bytes();
        let m = a.len();
        let n = b.len();
        let mut f = vec![vec![0i32; n + 1]; m + 1];
        let mut mx = 0;
        for i in 0..m {
            for j in 0..n {
                if a[i] == b[j] {
                    f[i + 1][j + 1] = f[i][j] + 1;
                    mx = mx.max(f[i + 1][j + 1]);
                }
            }
        }
        m as i32 + n as i32 - 2 * mx
    }
}
