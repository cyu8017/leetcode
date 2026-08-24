// LeetCode 0825 - Friends Of Appropriate Ages
// https://leetcode.com/problems/friends-of-appropriate-ages/

impl Solution {
    pub fn num_friend_requests(ages: Vec<i32>) -> i32 {
        let mut count = vec![0i32; 121];
        for age in ages {
            count[age as usize] += 1;
        }
        let mut ans = 0;
        for x in 1..=120 {
            if count[x] == 0 {
                continue;
            }
            for y in 1..=120 {
                if count[y] == 0 {
                    continue;
                }
                if (y as f64) <= 0.5 * (x as f64) + 7.0 || y > x || (y > 100 && x < 100) {
                    continue;
                }
                ans += count[x] * count[y];
                if x == y {
                    ans -= count[x];
                }
            }
        }
        ans
    }
}
