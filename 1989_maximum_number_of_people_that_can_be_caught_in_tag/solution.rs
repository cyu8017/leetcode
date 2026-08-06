// LeetCode 1989 - Maximum Number of People That Can Be Caught in Tag
// https://leetcode.com/problems/maximum-number-of-people-that-can-be-caught-in-tag/

impl Solution {
    pub fn catch_maximum_amountof_people(team: Vec<i32>, dist: i32) -> i32 {
        let mut ans = 0;
        let mut j = 0usize;
        let n = team.len();
        for (i, &x) in team.iter().enumerate() {
            if x != 0 {
                while j < n && (team[j] != 0 || (i as i32) - (j as i32) > dist) {
                    j += 1;
                }
                if j < n && ((i as i32) - (j as i32)).abs() <= dist {
                    ans += 1;
                    j += 1;
                }
            }
        }
        ans
    }
}
