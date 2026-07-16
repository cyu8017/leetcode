// LeetCode 0539 - Minimum Time Difference
// https://leetcode.com/problems/minimum-time-difference/

impl Solution {
    pub fn find_min_difference(time_points: Vec<String>) -> i32 {
        let mut minutes: Vec<i32> = time_points
            .iter()
            .map(|time| {
                let parts: Vec<&str> = time.split(':').collect();
                let hour: i32 = parts[0].parse().unwrap();
                let minute: i32 = parts[1].parse().unwrap();
                hour * 60 + minute
            })
            .collect();

        minutes.sort_unstable();
        let mut best = minutes.last().unwrap() - minutes.first().unwrap();
        for index in 1..minutes.len() {
            best = best.min(minutes[index] - minutes[index - 1]);
        }
        best.min(24 * 60 - minutes.last().unwrap() + minutes.first().unwrap())
    }
}
