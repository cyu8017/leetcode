struct Solution;
// LeetCode 3206 - Alternating Groups I
// https://leetcode.com/problems/alternating-groups-i/

impl Solution {
    pub fn number_of_alternating_groups(colors: Vec<i32>) -> i32 {
        let k = 3;
        let n = colors.len();
        let mut cnt = 0;
        let mut ans = 0;
        for i in 0..n * 2 {
            if i > 0 && colors[i % n] == colors[(i - 1) % n] {
                cnt = 1;
            } else {
                cnt += 1;
            }
            if i >= n && cnt >= k {
                ans += 1;
            }
        }
        ans
    }
}

fn main() {}
