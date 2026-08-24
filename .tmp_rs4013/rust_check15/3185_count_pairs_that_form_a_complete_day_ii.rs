struct Solution;
// LeetCode 3185 - Count Pairs That Form a Complete Day II
// https://leetcode.com/problems/count-pairs-that-form-a-complete-day-ii/

impl Solution {
    pub fn count_complete_day_pairs(hours: Vec<i32>) -> i64 {
        let mut cnt = [0i64; 24];
        let mut ans = 0i64;
        for x in hours {
            ans += cnt[(24 - x % 24) as usize % 24];
            cnt[(x % 24) as usize] += 1;
        }
        ans
    }
}

fn main() {}
