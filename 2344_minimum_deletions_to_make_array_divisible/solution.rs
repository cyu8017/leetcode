// LeetCode 2344 - Minimum Deletions to Make Array Divisible
// https://leetcode.com/problems/minimum-deletions-to-make-array-divisible/

impl Solution {
    pub fn min_operations(mut nums: Vec<i32>, nums_divide: Vec<i32>) -> i32 {
        fn gcd(mut a: i32, mut b: i32) -> i32 {
            while b != 0 {
                let t = a % b;
                a = b;
                b = t;
            }
            a
        }
        let mut g = nums_divide[0];
        for &x in nums_divide.iter().skip(1) {
            g = gcd(g, x);
        }
        nums.sort_unstable();
        for (i, &x) in nums.iter().enumerate() {
            if g % x == 0 {
                return i as i32;
            }
        }
        -1
    }
}
