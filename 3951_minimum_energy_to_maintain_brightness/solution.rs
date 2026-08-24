// LeetCode 3951 - Minimum Energy To Maintain Brightness
// https://leetcode.com/problems/minimum-energy-to-maintain-brightness/

impl Solution {
    pub fn min_energy(_n: i32, brightness: i32, mut intervals: Vec<Vec<i32>>) -> i64 {
        intervals.sort_by_key(|a| a[0]);
        let mut merged = vec![intervals[0].clone()];
        for x in intervals.into_iter().skip(1) {
            if merged.last().unwrap()[1] < x[0] {
                merged.push(x);
            } else if x[1] > merged.last().unwrap()[1] {
                merged.last_mut().unwrap()[1] = x[1];
            }
        }
        let mut ans = 0i64;
        for interval in merged {
            let m = interval[1] - interval[0] + 1;
            ans += ((brightness + 2) / 3) as i64 * m as i64;
        }
        ans
    }
}
