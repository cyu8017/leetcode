// LeetCode 1177 - Can Make Palindrome from Substring
// https://leetcode.com/problems/can-make-palindrome-from-substring/

impl Solution {
    pub fn can_make_pali_queries(s: String, queries: Vec<Vec<i32>>) -> Vec<bool> {
        let bytes = s.as_bytes();
        let mut prefix = vec![0; bytes.len() + 1];
        let mut mask = 0;
        for i in 0..bytes.len() {
            mask ^= 1 << (bytes[i] - b'a');
            prefix[i + 1] = mask;
        }
        queries
            .into_iter()
            .map(|q| {
                let bits = (prefix[q[1] as usize + 1] ^ prefix[q[0] as usize]).count_ones() as i32;
                bits / 2 <= q[2]
            })
            .collect()
    }
}
