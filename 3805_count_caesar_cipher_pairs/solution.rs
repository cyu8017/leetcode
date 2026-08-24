// LeetCode 3805 - Count Caesar Cipher Pairs
// https://leetcode.com/problems/count-caesar-cipher-pairs/

use std::collections::HashMap;

impl Solution {
    pub fn count_pairs(words: Vec<String>) -> i64 {
        let mut cnt: HashMap<String, i32> = HashMap::new();
        for s in words {
            let mut bytes = s.into_bytes();
            let k = (b'z' - bytes[0]) as i32;
            for i in 1..bytes.len() {
                bytes[i] = b'a' + ((bytes[i] - b'a') as i32 + k).rem_euclid(26) as u8;
            }
            bytes[0] = b'z';
            *cnt.entry(String::from_utf8(bytes).unwrap()).or_insert(0) += 1;
        }
        let mut ans = 0i64;
        for &v in cnt.values() {
            ans += v as i64 * (v as i64 - 1) / 2;
        }
        ans
    }
}
