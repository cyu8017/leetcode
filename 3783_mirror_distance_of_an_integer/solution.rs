// LeetCode 3783 - Mirror Distance Of An Integer
// https://leetcode.com/problems/mirror-distance-of-an-integer/

impl Solution {
    pub fn mirror_distance(n: i32) -> i32 {
        let reverse = |mut x: i32| {
            let mut y = 0;
            while x > 0 {
                y = y * 10 + x % 10;
                x /= 10;
            }
            y
        };
        (n - reverse(n)).abs()
    }
}
