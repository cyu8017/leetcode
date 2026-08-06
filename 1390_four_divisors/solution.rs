// LeetCode 1390 - Four Divisors
// https://leetcode.com/problems/four-divisors/

impl Solution {
    pub fn sum_four_divisors(nums: Vec<i32>) -> i32 {
        let mut ans = 0;
        for x in nums {
            let mut ds = std::collections::HashSet::new();
            let lim = (x as f64).sqrt() as i32;
            for d in 1..=lim {
                if x % d == 0 {
                    ds.insert(d);
                    ds.insert(x / d);
                }
                if ds.len() > 4 {
                    break;
                }
            }
            if ds.len() == 4 {
                ans += ds.into_iter().sum::<i32>();
            }
        }
        ans
    }
}
