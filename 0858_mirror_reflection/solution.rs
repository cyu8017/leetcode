// LeetCode 0858 - Mirror Reflection
// https://leetcode.com/problems/mirror-reflection/

impl Solution {
    pub fn mirror_reflection(mut p: i32, mut q: i32) -> i32 {
        fn gcd(mut a: i32, mut b: i32) -> i32 {
            while b != 0 {
                let t = a % b;
                a = b;
                b = t;
            }
            a
        }
        let g = gcd(p, q);
        p /= g;
        q /= g;
        if p % 2 == 0 {
            return 2;
        }
        if q % 2 == 0 {
            return 0;
        }
        1
    }
}
