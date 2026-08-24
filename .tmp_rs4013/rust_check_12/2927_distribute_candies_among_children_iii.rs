struct Solution;
// LeetCode 2927 - Distribute Candies Among Children III
// https://leetcode.com/problems/distribute-candies-among-children-iii/

impl Solution {
    pub fn distribute_candies(n: i32, limit: i32) -> i64 {
        let comb = |x: i64| -> i64 {
            if x < 2 {
                0
            } else {
                x * (x - 1) / 2
            }
        };
        let n = n as i64;
        let limit = limit as i64;
        let mut ans = comb(n + 2);
        ans -= 3 * comb(n - limit + 1);
        ans += 3 * comb(n - 2 * (limit + 1) + 2);
        ans -= comb(n - 3 * (limit + 1) + 2);
        if ans < 0 {
            ans = 0;
        }
        ans
    }
}

fn main() {}
