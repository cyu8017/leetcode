// LeetCode 3893 - Maximum Team Size With Overlapping Intervals
// https://leetcode.com/problems/maximum-team-size-with-overlapping-intervals/

impl Solution {
    pub fn maximum_team_size(start_time: Vec<i32>, end_time: Vec<i32>) -> i32 {
        let n = start_time.len();
        let mut intervals = Vec::with_capacity(n);
        for i in 0..n {
            intervals.push((start_time[i], end_time[i]));
        }
        let mut st = start_time;
        let mut en = end_time;
        st.sort_unstable();
        en.sort_unstable();
        let mut ans = 0;
        for &(l, r) in &intervals {
            let i = en.partition_point(|&x| x <= l - 1);
            let j = st.partition_point(|&x| x <= r);
            ans = ans.max((j - i) as i32);
        }
        ans
    }
}
