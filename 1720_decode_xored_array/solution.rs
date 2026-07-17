// LeetCode 1720 - Decode XORed Array
// https://leetcode.com/problems/decode-xored-array/

impl Solution {
    pub fn decode(encoded: Vec<i32>, first: i32) -> Vec<i32> {
        let mut ans = Vec::with_capacity(encoded.len() + 1);
        ans.push(first);
        for value in encoded {
            ans.push(ans[ans.len() - 1] ^ value);
        }
        ans
    }
}
