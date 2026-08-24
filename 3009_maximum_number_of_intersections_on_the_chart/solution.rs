// LeetCode 3009 - Maximum Number of Intersections on the Chart
// https://leetcode.com/problems/maximum-number-of-intersections-on-the-chart/

use std::collections::BTreeMap;

impl Solution {
    pub fn max_intersection_count(y: Vec<i32>) -> i32 {
        let n = y.len();
        let mut line: BTreeMap<i32, i32> = BTreeMap::new();
        for i in 1..n {
            let start = 2 * y[i - 1];
            let mut end = 2 * y[i];
            if i != n - 1 {
                if y[i] > y[i - 1] {
                    end -= 1;
                } else {
                    end += 1;
                }
            }
            let (a, b) = if start <= end { (start, end) } else { (end, start) };
            *line.entry(a).or_insert(0) += 1;
            *line.entry(b + 1).or_insert(0) -= 1;
        }
        let mut ans = 0;
        let mut cur = 0;
        for (_, v) in line {
            cur += v;
            if cur > ans {
                ans = cur;
            }
        }
        ans
    }
}
