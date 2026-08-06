// LeetCode 1250 - Check If It Is a Good Array
// https://leetcode.com/problems/check-if-it-is-a-good-array/

impl Solution {
    pub fn is_good_array(nums: Vec<i32>) -> bool {
        fn gcd(mut a: i32, mut b: i32) -> i32 {
            while b != 0 {
                let t = a % b;
                a = b;
                b = t;
            }
            a
        }
        let mut g = nums[0];
        for &x in &nums[1..] {
            g = gcd(g, x);
        }
        g == 1
    }
}
