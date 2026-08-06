// LeetCode 1229 - Meeting Scheduler
// https://leetcode.com/problems/meeting-scheduler/

impl Solution {
    pub fn min_available_duration(
        mut slots1: Vec<Vec<i32>>,
        mut slots2: Vec<Vec<i32>>,
        duration: i32,
    ) -> Vec<i32> {
        slots1.sort_by_key(|s| s[0]);
        slots2.sort_by_key(|s| s[0]);
        let mut i = 0;
        let mut j = 0;
        while i < slots1.len() && j < slots2.len() {
            let start = slots1[i][0].max(slots2[j][0]);
            let end = slots1[i][1].min(slots2[j][1]);
            if end - start >= duration {
                return vec![start, start + duration];
            }
            if slots1[i][1] < slots2[j][1] {
                i += 1;
            } else {
                j += 1;
            }
        }
        vec![]
    }
}
