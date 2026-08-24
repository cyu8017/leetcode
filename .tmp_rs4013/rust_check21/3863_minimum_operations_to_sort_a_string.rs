struct Solution;
// LeetCode 3863 - Minimum Operations to Sort a String
// https://leetcode.com/problems/minimum-operations-to-sort-a-string/

impl Solution {
    pub fn min_operations(s: String) -> i32 {
        let b = s.as_bytes();
        let n = b.len();
        let sorted = b.windows(2).all(|w| w[1] >= w[0]);
        if sorted {
            return 0;
        }
        if n == 2 {
            return -1;
        }
        let mn = *b.iter().min().unwrap();
        let mx = *b.iter().max().unwrap();
        if b[0] == mn || b[n - 1] == mx {
            return 1;
        }
        for i in 1..n - 1 {
            if b[i] == mn || b[i] == mx {
                return 2;
            }
        }
        3
    }
}
