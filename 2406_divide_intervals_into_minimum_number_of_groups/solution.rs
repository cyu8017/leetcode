// LeetCode 2406 - Divide Intervals Into Minimum Number of Groups
// https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/

impl Solution {
    pub fn min_groups(intervals: Vec<Vec<i32>>) -> i32 {
        let mut events = Vec::with_capacity(intervals.len() * 2);
        for it in intervals {
            events.push((it[0], 1));
            events.push((it[1] + 1, -1));
        }
        events.sort_unstable();
        let mut cur = 0;
        let mut ans = 0;
        for (_, d) in events {
            cur += d;
            ans = ans.max(cur);
        }
        ans
    }
}
