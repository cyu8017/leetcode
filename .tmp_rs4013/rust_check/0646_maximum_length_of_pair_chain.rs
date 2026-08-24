struct Solution;
// LeetCode 0646 - Maximum Length of Pair Chain
// https://leetcode.com/problems/maximum-length-of-pair-chain/

impl Solution {
    pub fn find_longest_chain(mut pairs: Vec<Vec<i32>>) -> i32 {
        pairs.sort_by_key(|p| p[1]);
        let mut length = 0;
        let mut current_end = i32::MIN;
        for pair in pairs {
            if pair[0] > current_end {
                length += 1;
                current_end = pair[1];
            }
        }
        length
    }
}

fn main() {}
