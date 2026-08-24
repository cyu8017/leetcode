// LeetCode 2125 - Number of Laser Beams in a Bank
// https://leetcode.com/problems/number-of-laser-beams-in-a-bank/

impl Solution {
    pub fn number_of_beams(bank: Vec<String>) -> i32 {
        let mut ans = 0;
        let mut prev = 0;
        for row in bank {
            let cnt = row.bytes().filter(|&c| c == b'1').count() as i32;
            if cnt > 0 {
                ans += prev * cnt;
                prev = cnt;
            }
        }
        ans
    }
}
