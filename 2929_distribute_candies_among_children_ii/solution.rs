// LeetCode 2929 - Distribute Candies Among Children II
// https://leetcode.com/problems/distribute-candies-among-children-ii/

impl Solution {
    pub fn distribute_candies(n: i32, limit: i32) -> i64 {
        let comb2 = |x: i64| -> i64 {
            if x < 0 {
                0
            } else {
                (x + 1) * (x + 2) / 2
            }
        };
        let n = n as i64;
        let limit = limit as i64;
        let mut ans = comb2(n);
        ans -= 3 * comb2(n - (limit + 1));
        ans += 3 * comb2(n - 2 * (limit + 1));
        ans -= comb2(n - 3 * (limit + 1));
        ans
    }
}
