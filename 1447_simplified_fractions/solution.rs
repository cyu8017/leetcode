// LeetCode 1447 - Simplified Fractions
// https://leetcode.com/problems/simplified-fractions/

impl Solution {
    pub fn simplified_fractions(n: i32) -> Vec<String> {
        fn gcd(mut a: i32, mut b: i32) -> i32 {
            while b != 0 {
                let t = a % b;
                a = b;
                b = t;
            }
            a
        }
        let mut answer = Vec::new();
        for a in 1..n {
            for b in a + 1..=n {
                if gcd(a, b) == 1 {
                    answer.push(format!("{}/{}", a, b));
                }
            }
        }
        answer
    }
}
