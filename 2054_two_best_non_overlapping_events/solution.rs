// LeetCode 2054 - Two Best Non-Overlapping Events
// https://leetcode.com/problems/two-best-non-overlapping-events/

impl Solution {
    pub fn max_two_events(mut events: Vec<Vec<i32>>) -> i32 {
        events.sort_unstable();
        let n = events.len();
        let mut suffix = vec![0; n + 1];
        for i in (0..n).rev() {
            suffix[i] = suffix[i + 1].max(events[i][2]);
        }
        let mut ans = 0;
        for i in 0..n {
            ans = ans.max(events[i][2]);
            let mut lo = i + 1;
            let mut hi = n;
            while lo < hi {
                let mid = (lo + hi) / 2;
                if events[mid][0] > events[i][1] {
                    hi = mid;
                } else {
                    lo = mid + 1;
                }
            }
            if lo < n {
                ans = ans.max(events[i][2] + suffix[lo]);
            }
        }
        ans
    }
}
