// LeetCode 1849 - Splitting a String Into Descending Consecutive Values
// https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/

impl Solution {
    pub fn split_string(s: String) -> bool {
        fn dfs(s: &[u8], index: usize, previous: Option<u128>, parts: i32) -> bool {
            if index == s.len() {
                return parts >= 2;
            }

            let mut value: u128 = 0;
            for end in index..s.len() {
                value = value * 10 + (s[end] - b'0') as u128;
                match previous {
                    None => {
                        if dfs(s, end + 1, Some(value), parts + 1) {
                            return true;
                        }
                    }
                    Some(prev) => {
                        if prev > 0 && value == prev - 1 {
                            if dfs(s, end + 1, Some(value), parts + 1) {
                                return true;
                            }
                        } else if prev == 0 || value > prev - 1 {
                            break;
                        }
                    }
                }
            }
            false
        }

        dfs(s.as_bytes(), 0, None, 0)
    }
}
