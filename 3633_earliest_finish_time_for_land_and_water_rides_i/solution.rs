// LeetCode 3633 - Earliest Finish Time for Land and Water Rides I
// https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-i/

impl Solution {
    fn calc(a1: &[i32], t1: &[i32], a2: &[i32], t2: &[i32]) -> i32 {
        let mut min_end = i32::MAX;
        for i in 0..a1.len() {
            min_end = min_end.min(a1[i] + t1[i]);
        }
        let mut ans = i32::MAX;
        for i in 0..a2.len() {
            ans = ans.min(min_end.max(a2[i]) + t2[i]);
        }
        ans
    }

    pub fn earliest_finish_time(
        land_start_time: Vec<i32>,
        land_duration: Vec<i32>,
        water_start_time: Vec<i32>,
        water_duration: Vec<i32>,
    ) -> i32 {
        Self::calc(&land_start_time, &land_duration, &water_start_time, &water_duration).min(Self::calc(
            &water_start_time,
            &water_duration,
            &land_start_time,
            &land_duration,
        ))
    }
}
