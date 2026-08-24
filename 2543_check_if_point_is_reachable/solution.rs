// LeetCode 2543 - Check if Point Is Reachable
// https://leetcode.com/problems/check-if-point-is-reachable/

impl Solution {
    pub fn is_reachable(target_x: i32, target_y: i32) -> bool {
        fn gcd(mut a: i32, mut b: i32) -> i32 {
            while b != 0 {
                let t = a % b;
                a = b;
                b = t;
            }
            a
        }
        let mut g = gcd(target_x, target_y);
        while g % 2 == 0 {
            g /= 2;
        }
        g == 1
    }
}
