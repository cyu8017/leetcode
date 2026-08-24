// LeetCode 2580 - Count Ways to Group Overlapping Ranges
// https://leetcode.com/problems/count-ways-to-group-overlapping-ranges/

impl Solution {
    pub fn count_ways(mut ranges: Vec<Vec<i32>>) -> i32 {
        const MOD: i32 = 1_000_000_007;
        ranges.sort_unstable();
        let mut groups = 0;
        let mut end = -1;
        for r in ranges {
            if r[0] > end {
                groups += 1;
                end = r[1];
            } else if r[1] > end {
                end = r[1];
            }
        }
        let mut ans = 1i32;
        for _ in 0..groups {
            ans = ans * 2 % MOD;
        }
        ans
    }
}
