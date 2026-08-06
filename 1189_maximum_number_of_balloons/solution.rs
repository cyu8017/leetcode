// LeetCode 1189 - Maximum Number of Balloons
// https://leetcode.com/problems/maximum-number-of-balloons/

impl Solution {
    pub fn max_number_of_balloons(text: String) -> i32 {
        let mut count = [0; 26];
        for b in text.bytes() {
            count[(b - b'a') as usize] += 1;
        }
        *[
            count[(b'b' - b'a') as usize],
            count[(b'a' - b'a') as usize],
            count[(b'l' - b'a') as usize] / 2,
            count[(b'o' - b'a') as usize] / 2,
            count[(b'n' - b'a') as usize],
        ]
        .iter()
        .min()
        .unwrap()
    }
}
