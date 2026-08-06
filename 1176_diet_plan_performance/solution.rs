// LeetCode 1176 - Diet Plan Performance
// https://leetcode.com/problems/diet-plan-performance/

impl Solution {
    pub fn diet_plan_performance(calories: Vec<i32>, k: i32, lower: i32, upper: i32) -> i32 {
        let k = k as usize;
        let mut window: i32 = calories[..k].iter().sum();
        let mut ans = 0;
        if window < lower {
            ans -= 1;
        } else if window > upper {
            ans += 1;
        }
        for i in k..calories.len() {
            window += calories[i] - calories[i - k];
            if window < lower {
                ans -= 1;
            } else if window > upper {
                ans += 1;
            }
        }
        ans
    }
}
