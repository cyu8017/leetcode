struct Solution;
// LeetCode 3460 - Longest Common Prefix After at Most One Removal
// https://leetcode.com/problems/longest-common-prefix-after-at-most-one-removal/

impl Solution {
    pub fn longest_common_prefix(s: String, t: String) -> i32 {
        let sb = s.as_bytes();
        let tb = t.as_bytes();
        let mut i = 0;
        let mut j = 0;
        let mut removed = false;
        while i < sb.len() && j < tb.len() {
            if sb[i] == tb[j] {
                i += 1;
                j += 1;
                continue;
            }
            if removed {
                break;
            }
            removed = true;
            i += 1;
        }
        j as i32
    }
}

fn main() {}
