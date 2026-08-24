struct Solution;
// LeetCode 2895 - Minimum Processing Time
// https://leetcode.com/problems/minimum-processing-time/

impl Solution {
    pub fn min_processing_time(mut processor_time: Vec<i32>, mut tasks: Vec<i32>) -> i32 {
        processor_time.sort_unstable();
        tasks.sort_unstable_by(|a, b| b.cmp(a));
        let mut ans = 0;
        for i in 0..processor_time.len() {
            ans = ans.max(processor_time[i] + tasks[i * 4]);
        }
        ans
    }
}

fn main() {}
