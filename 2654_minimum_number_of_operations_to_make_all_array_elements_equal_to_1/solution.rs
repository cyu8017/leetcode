// LeetCode 2654 - Minimum Number of Operations to Make All Array Elements Equal to 1
// https://leetcode.com/problems/minimum-number-of-operations-to-make-all-array-elements-equal-to-1/

impl Solution {
    pub fn min_operations(nums: Vec<i32>) -> i32 {
        fn gcd(mut a: i32, mut b: i32) -> i32 {
            while b != 0 {
                let t = a % b;
                a = b;
                b = t;
            }
            a
        }
        let n = nums.len() as i32;
        let ones = nums.iter().filter(|&&x| x == 1).count() as i32;
        if ones > 0 {
            return n - ones;
        }
        let mut best = n + 1;
        for i in 0..nums.len() {
            let mut g = 0;
            for j in i..nums.len() {
                g = gcd(g, nums[j]);
                if g == 1 {
                    best = best.min((j - i) as i32);
                    break;
                }
            }
        }
        if best == n + 1 {
            -1
        } else {
            best + n - 1
        }
    }
}
