// LeetCode 2156 - Find Substring With Given Hash Value
// https://leetcode.com/problems/find-substring-with-given-hash-value/

impl Solution {
    pub fn sub_str_hash(s: String, power: i32, modulo: i32, k: i32, hash_value: i32) -> String {
        let n = s.len();
        let k = k as usize;
        let power = power as i64;
        let modulo = modulo as i64;
        let hash_value = hash_value as i64;
        let b = s.as_bytes();
        let mut pk = 1i64;
        for _ in 0..k - 1 {
            pk = pk * power % modulo;
        }
        let mut h = 0i64;
        let mut ans = 0;
        for i in (n - k..n).rev() {
            h = (h * power + (b[i] - b'a' + 1) as i64) % modulo;
        }
        if h == hash_value {
            ans = n - k;
        }
        for i in (0..n - k).rev() {
            h = (h - (b[i + k] - b'a' + 1) as i64 * pk % modulo + modulo) % modulo;
            h = (h * power + (b[i] - b'a' + 1) as i64) % modulo;
            if h == hash_value {
                ans = i;
            }
        }
        s[ans..ans + k].to_string()
    }
}
