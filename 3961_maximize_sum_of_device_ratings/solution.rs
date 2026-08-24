// LeetCode 3961 - Maximize Sum Of Device Ratings
// https://leetcode.com/problems/maximize-sum-of-device-ratings/

impl Solution {
    pub fn max_ratings(mut units: Vec<Vec<i32>>) -> i64 {
        let n = units[0].len();
        if n == 1 {
            let mut ans = 0i64;
            for x in &units {
                ans += x[0] as i64;
            }
            return ans;
        }
        let mut ans = 0i64;
        let mut mn = i32::MAX;
        let mut mn2 = i32::MAX;
        for x in units.iter_mut() {
            x.sort_unstable();
            ans += x[1] as i64;
            mn2 = mn2.min(x[1]);
            mn = mn.min(x[0]);
        }
        ans - (mn2 - mn) as i64
    }
}
