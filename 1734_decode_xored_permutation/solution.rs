// LeetCode 1734 - Decode XORed Permutation
// https://leetcode.com/problems/decode-xored-permutation/

impl Solution {
    pub fn decode(encoded: Vec<i32>) -> Vec<i32> {
        let n = encoded.len() as i32 + 1;
        let mut total = 0;
        for value in 1..=n {
            total ^= value;
        }
        let mut odd = 0;
        for i in (1..encoded.len()).step_by(2) {
            odd ^= encoded[i];
        }
        let mut ans = Vec::with_capacity(encoded.len() + 1);
        ans.push(total ^ odd);
        for &value in &encoded {
            ans.push(ans[ans.len() - 1] ^ value);
        }
        ans
    }
}
