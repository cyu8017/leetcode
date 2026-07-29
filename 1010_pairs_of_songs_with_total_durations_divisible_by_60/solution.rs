// LeetCode 1010 - Pairs of Songs With Total Durations Divisible by 60
// https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/

impl Solution {
    pub fn num_pairs_divisible_by60(time: Vec<i32>) -> i32 {
        let mut count = [0i32; 60];
        let mut ans = 0;
        for t in time {
            let rem = t.rem_euclid(60) as usize;
            let need = (60 - rem) % 60;
            ans += count[need];
            count[rem] += 1;
        }
        ans
    }
}
