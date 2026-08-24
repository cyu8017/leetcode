// LeetCode 2197 - Replace Non-Coprime Numbers in Array
// https://leetcode.com/problems/replace-non-coprime-numbers-in-array/

impl Solution {
    pub fn replace_non_coprimes(nums: Vec<i32>) -> Vec<i32> {
        fn gcd(mut a: i64, mut b: i64) -> i64 {
            while b != 0 {
                let t = a % b;
                a = b;
                b = t;
            }
            a
        }
        let mut stack: Vec<i64> = Vec::new();
        for x0 in nums {
            let mut x = x0 as i64;
            while let Some(&last) = stack.last() {
                let g = gcd(last, x);
                if g == 1 {
                    break;
                }
                x = last / g * x;
                stack.pop();
            }
            stack.push(x);
        }
        stack.into_iter().map(|x| x as i32).collect()
    }
}
