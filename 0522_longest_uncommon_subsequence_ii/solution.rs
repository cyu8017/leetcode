// LeetCode 0522 - Longest Uncommon Subsequence II
// https://leetcode.com/problems/longest-uncommon-subsequence-ii/

impl Solution {
    pub fn find_luslength(strs: Vec<String>) -> i32 {
        fn is_subsequence(target: &str, source: &str) -> bool {
            let mut index = 0;
            for ch in source.chars() {
                if index < target.len() && target.as_bytes()[index] == ch as u8 {
                    index += 1;
                }
            }
            index == target.len()
        }

        let mut result = -1;
        for (i, candidate) in strs.iter().enumerate() {
            let uncommon = strs
                .iter()
                .enumerate()
                .all(|(j, other)| i == j || !is_subsequence(candidate, other));
            if uncommon {
                result = result.max(candidate.len() as i32);
            }
        }
        result
    }
}
