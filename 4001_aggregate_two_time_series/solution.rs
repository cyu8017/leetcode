// LeetCode 4001 - Aggregate Two Time Series
// https://leetcode.com/problems/aggregate-two-time-series/

impl Solution {
    pub fn aggregate_time_series(
        series1: Vec<Vec<i32>>,
        series2: Vec<Vec<i32>>,
    ) -> Vec<Vec<i32>> {
        let m = series1.len();
        let n = series2.len();
        let mut i = 0;
        let mut j = 0;
        let mut ans = Vec::new();
        while i < m && j < n {
            let t1 = series1[i][0];
            let v1 = series1[i][1];
            let t2 = series2[j][0];
            let v2 = series2[j][1];
            if t1 == t2 {
                ans.push(vec![t1, v1 + v2]);
                i += 1;
                j += 1;
            } else if t1 < t2 {
                ans.push(vec![t1, v1 + v2]);
                i += 1;
            } else {
                ans.push(vec![t2, v1 + v2]);
                j += 1;
            }
        }
        while i < m {
            ans.push(series1[i].clone());
            i += 1;
        }
        while j < n {
            ans.push(series2[j].clone());
            j += 1;
        }
        ans
    }
}
