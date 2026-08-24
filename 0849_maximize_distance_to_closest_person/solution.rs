// LeetCode 0849 - Maximize Distance to Closest Person
// https://leetcode.com/problems/maximize-distance-to-closest-person/

impl Solution {
    pub fn max_dist_to_closest(seats: Vec<i32>) -> i32 {
        let n = seats.len() as i32;
        let mut prev = -1;
        let mut ans = 0;
        for i in 0..seats.len() {
            if seats[i] != 0 {
                if prev == -1 {
                    ans = i as i32;
                } else {
                    ans = ans.max((i as i32 - prev) / 2);
                }
                prev = i as i32;
            }
        }
        ans.max(n - 1 - prev)
    }
}
