struct Solution;
// LeetCode 0583 - Delete Operation for Two Strings
// https://leetcode.com/problems/delete-operation-for-two-strings/

impl Solution {
    pub fn min_distance(word1: String, word2: String) -> i32 {
        let w1 = word1.as_bytes();
        let w2 = word2.as_bytes();
        let m = w1.len();
        let n = w2.len();
        let mut prev = vec![0i32; n + 1];
        let mut curr = vec![0i32; n + 1];
        for i in 1..=m {
            for j in 1..=n {
                if w1[i - 1] == w2[j - 1] {
                    curr[j] = prev[j - 1] + 1;
                } else {
                    curr[j] = prev[j].max(curr[j - 1]);
                }
            }
            std::mem::swap(&mut prev, &mut curr);
            curr.fill(0);
        }
        (m + n) as i32 - 2 * prev[n]
    }
}

fn main() {}
