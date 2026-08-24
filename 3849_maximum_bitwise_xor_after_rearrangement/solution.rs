// LeetCode 3849 - Maximum Bitwise XOR After Rearrangement
// https://leetcode.com/problems/maximum-bitwise-xor-after-rearrangement/

impl Solution {
    pub fn maximum_xor(s: String, t: String) -> String {
        let mut cnt = [0; 2];
        for c in t.bytes() {
            cnt[(c - b'0') as usize] += 1;
        }
        let sb = s.as_bytes();
        let mut ans = vec![b'0'; sb.len()];
        for i in 0..sb.len() {
            let x = (sb[i] - b'0') as usize;
            if cnt[x ^ 1] > 0 {
                cnt[x ^ 1] -= 1;
                ans[i] = b'1';
            } else {
                cnt[x] -= 1;
                ans[i] = b'0';
            }
        }
        String::from_utf8(ans).unwrap()
    }
}
