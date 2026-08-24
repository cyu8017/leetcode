// LeetCode 3744 - Find Kth Character in Expanded String
// https://leetcode.com/problems/find-kth-character-in-expanded-string/

impl Solution {
    pub fn kth_character(s: String, mut k: i64) -> char {
        for w in s.split_whitespace() {
            let sz = w.len() as i64;
            let m = (1 + sz) * sz / 2;
            if k == m {
                return ' ';
            }
            if k > m {
                k -= m + 1;
            } else {
                let mut cur = 0i64;
                let bytes = w.as_bytes();
                let mut i = 0usize;
                loop {
                    cur += i as i64 + 1;
                    if k < cur {
                        return bytes[i] as char;
                    }
                    i += 1;
                }
            }
        }
        ' '
    }
}
