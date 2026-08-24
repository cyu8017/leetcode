// LeetCode 0955 - Delete Columns to Make Sorted II
// https://leetcode.com/problems/delete-columns-to-make-sorted-ii/

impl Solution {
    pub fn min_deletion_size(strs: Vec<String>) -> i32 {
        let n = strs.len();
        let m = strs[0].len();
        let mut deleted = 0;
        let mut sorted_pair = vec![false; n - 1];
        for c in 0..m {
            let mut bad = false;
            for r in 0..n - 1 {
                if !sorted_pair[r] && strs[r].as_bytes()[c] > strs[r + 1].as_bytes()[c] {
                    bad = true;
                    break;
                }
            }
            if bad {
                deleted += 1;
                continue;
            }
            for r in 0..n - 1 {
                if strs[r].as_bytes()[c] < strs[r + 1].as_bytes()[c] {
                    sorted_pair[r] = true;
                }
            }
        }
        deleted
    }
}
