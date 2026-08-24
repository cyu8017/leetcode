// LeetCode 2663 - Lexicographically Smallest Beautiful String
// https://leetcode.com/problems/lexicographically-smallest-beautiful-string/

impl Solution {
    pub fn smallest_beautiful_string(s: String, k: i32) -> String {
        let n = s.len();
        let mut b: Vec<u8> = s.into_bytes();
        for i in (0..n).rev() {
            let mut c = b[i] + 1;
            while c < b'a' + k as u8 {
                if (i > 0 && c == b[i - 1]) || (i > 1 && c == b[i - 2]) {
                    c += 1;
                    continue;
                }
                b[i] = c;
                for j in i + 1..n {
                    let mut nc = b'a';
                    while nc < b'a' + k as u8 {
                        if (j > 0 && nc == b[j - 1]) || (j > 1 && nc == b[j - 2]) {
                            nc += 1;
                            continue;
                        }
                        b[j] = nc;
                        break;
                    }
                }
                return String::from_utf8(b).unwrap();
            }
        }
        String::new()
    }
}
