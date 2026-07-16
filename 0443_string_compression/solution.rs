// LeetCode 0443 - String Compression
// https://leetcode.com/problems/string-compression/

impl Solution {
    pub fn compress(chars: &mut Vec<char>) -> i32 {
        let mut write = 0;
        let mut read = 0;
        while read < chars.len() {
            let ch = chars[read];
            let mut count = 0;
            while read < chars.len() && chars[read] == ch {
                read += 1;
                count += 1;
            }
            chars[write] = ch;
            write += 1;
            if count > 1 {
                for digit in count.to_string().chars() {
                    chars[write] = digit;
                    write += 1;
                }
            }
        }
        write as i32
    }
}
