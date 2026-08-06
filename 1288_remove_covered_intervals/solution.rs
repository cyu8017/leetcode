// LeetCode 1288 - Remove Covered Intervals
// https://leetcode.com/problems/remove-covered-intervals/

impl Solution {
    pub fn remove_covered_intervals(mut intervals: Vec<Vec<i32>>) -> i32 {
        intervals.sort_by(|a, b| a[0].cmp(&b[0]).then_with(|| b[1].cmp(&a[1])));
        let mut answer = 0;
        let mut farthest = -1;
        for iv in intervals {
            if iv[1] > farthest {
                answer += 1;
                farthest = iv[1];
            }
        }
        answer
    }
}
