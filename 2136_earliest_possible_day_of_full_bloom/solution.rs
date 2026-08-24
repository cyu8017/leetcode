// LeetCode 2136 - Earliest Possible Day of Full Bloom
// https://leetcode.com/problems/earliest-possible-day-of-full-bloom/

impl Solution {
    pub fn earliest_full_bloom(plant_time: Vec<i32>, grow_time: Vec<i32>) -> i32 {
        let n = plant_time.len();
        let mut idx: Vec<usize> = (0..n).collect();
        idx.sort_by(|&a, &b| grow_time[b].cmp(&grow_time[a]));
        let mut day = 0;
        let mut ans = 0;
        for i in idx {
            day += plant_time[i];
            ans = ans.max(day + grow_time[i]);
        }
        ans
    }
}
