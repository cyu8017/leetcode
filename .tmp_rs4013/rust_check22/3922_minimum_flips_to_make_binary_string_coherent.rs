struct Solution;
// LeetCode 3922 - Minimum Flips to Make Binary String Coherent
// https://leetcode.com/problems/minimum-flips-to-make-binary-string-coherent/

impl Solution {
    pub fn min_flips(s: String) -> i32 {
        let bytes = s.as_bytes();
        let ones = bytes.iter().filter(|&&c| c == b'1').count() as i32;
        let mut answer = ones;
        if ones > 0 {
            answer = ones - 1;
        }
        let zeros = bytes.len() as i32 - ones;
        answer = answer.min(zeros);
        if bytes.len() >= 2 {
            let mut cost = 0;
            for i in 0..bytes.len() {
                let want = if i == 0 || i + 1 == bytes.len() { b'1' } else { b'0' };
                if bytes[i] != want {
                    cost += 1;
                }
            }
            answer = answer.min(cost);
        }
        answer
    }
}

fn main() {}
