// LeetCode 1904 - The Number of Full Rounds You Have Played
// https://leetcode.com/problems/the-number-of-full-rounds-you-have-played/

impl Solution {
    pub fn number_of_rounds(login_time: String, logout_time: String) -> i32 {
        fn to_min(t: &str) -> i32 {
            let parts: Vec<i32> = t.split(':').map(|x| x.parse().unwrap()).collect();
            parts[0] * 60 + parts[1]
        }

        let start = to_min(&login_time);
        let mut end = to_min(&logout_time);
        if end < start {
            end += 24 * 60;
        }
        let start = (start + 14) / 15 * 15;
        let end = end / 15 * 15;
        ((end - start) / 15).max(0)
    }
}
