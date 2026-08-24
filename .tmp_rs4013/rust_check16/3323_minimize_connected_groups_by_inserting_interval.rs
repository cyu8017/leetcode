struct Solution;
// LeetCode 3323 - Minimize Connected Groups by Inserting Interval
// https://leetcode.com/problems/minimize-connected-groups-by-inserting-interval/

impl Solution {
    pub fn min_connected_groups(mut intervals: Vec<Vec<i32>>, k: i32) -> i32 {
        intervals.sort_unstable();
        let mut merged: Vec<Vec<i32>> = Vec::new();
        for it in intervals {
            if merged.is_empty() || it[0] > merged.last().unwrap()[1] {
                merged.push(vec![it[0], it[1]]);
            } else if it[1] > merged.last().unwrap()[1] {
                merged.last_mut().unwrap()[1] = it[1];
            }
        }
        let m = merged.len();
        let mut ans = m as i32;
        for i in 0..m {
            let end = merged[i][1] + k;
            let mut j = i;
            while j < m && merged[j][0] <= end {
                j += 1;
            }
            let groups = i as i32 + 1 + (m - j) as i32;
            if groups < ans {
                ans = groups;
            }
        }
        ans
    }
}

fn main() {}
