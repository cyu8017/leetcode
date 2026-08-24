struct Solution;
// LeetCode 3184 - Count Pairs That Form a Complete Day I
// https://leetcode.com/problems/count-pairs-that-form-a-complete-day-i/

impl Solution {
    pub fn count_complete_day_pairs(hours: Vec<i32>) -> i32 {
        let mut cnt = [0; 24];
        let mut ans = 0;
        for x in hours {
            ans += cnt[(24 - x % 24) as usize % 24];
            cnt[(x % 24) as usize] += 1;
        }
        ans
    }
}

fn main() {}
