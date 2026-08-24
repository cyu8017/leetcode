struct Solution;
fn main() {}

// LeetCode 2748 - Number of Beautiful Pairs
// https://leetcode.com/problems/number-of-beautiful-pairs/

impl Solution {
    pub fn count_beautiful_pairs(nums: Vec<i32>) -> i32 {
        fn gcd(mut a: i32, mut b: i32) -> i32 {
            while b != 0 {
                let t = a % b;
                a = b;
                b = t;
            }
            a
        }
        fn first_digit(mut x: i32) -> i32 {
            while x >= 10 {
                x /= 10;
            }
            x
        }
        let mut ans = 0;
        let mut freq = [0i32; 10];
        for x in nums {
            let last = x % 10;
            for d in 1..=9 {
                if freq[d as usize] > 0 && gcd(d, last) == 1 {
                    ans += freq[d as usize];
                }
            }
            freq[first_digit(x) as usize] += 1;
        }
        ans
    }
}
