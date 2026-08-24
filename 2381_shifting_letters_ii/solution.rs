// LeetCode 2381 - Shifting Letters II
// https://leetcode.com/problems/shifting-letters-ii/

impl Solution {
    pub fn shifting_letters(s: String, shifts: Vec<Vec<i32>>) -> String {
        let n = s.len();
        let mut diff = vec![0i32; n + 1];
        for sh in shifts {
            let d = if sh[2] == 0 { -1 } else { 1 };
            diff[sh[0] as usize] += d;
            diff[sh[1] as usize + 1] -= d;
        }
        let mut cur = 0i32;
        let mut bytes = s.into_bytes();
        for i in 0..n {
            cur = (cur + diff[i]) % 26;
            if cur < 0 {
                cur += 26;
            }
            bytes[i] = b'a' + (bytes[i] - b'a' + cur as u8) % 26;
        }
        String::from_utf8(bytes).unwrap()
    }
}
