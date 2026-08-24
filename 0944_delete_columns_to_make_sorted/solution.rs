// LeetCode 0944 - Delete Columns to Make Sorted
// https://leetcode.com/problems/delete-columns-to-make-sorted/

impl Solution {
    pub fn min_deletion_size(strs: Vec<String>) -> i32 {
        let n = strs.len();
        let m = strs[0].len();
        let mut ans = 0;
        for c in 0..m {
            for r in 0..n - 1 {
                if strs[r].as_bytes()[c] > strs[r + 1].as_bytes()[c] {
                    ans += 1;
                    break;
                }
            }
        }
        ans
    }
}
