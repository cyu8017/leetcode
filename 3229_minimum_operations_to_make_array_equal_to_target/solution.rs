// LeetCode 3229 - Minimum Operations to Make Array Equal to Target
// https://leetcode.com/problems/minimum-operations-to-make-array-equal-to-target/

impl Solution {
    pub fn minimum_operations(nums: Vec<i32>, target: Vec<i32>) -> i64 {
        let absv = |x: i32| if x < 0 { -x } else { x };
        let mut f = absv(target[0] - nums[0]) as i64;
        for i in 1..target.len() {
            let x = target[i] - nums[i];
            let y = target[i - 1] - nums[i - 1];
            if x as i64 * y as i64 > 0 {
                let d = absv(x) - absv(y);
                if d > 0 {
                    f += d as i64;
                }
            } else {
                f += absv(x) as i64;
            }
        }
        f
    }
}
