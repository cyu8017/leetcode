struct Solution;
// LeetCode 2443 - Sum of Number and Its Reverse
// https://leetcode.com/problems/sum-of-number-and-its-reverse/

impl Solution {
    pub fn sum_of_number_and_reverse(num: i32) -> bool {
        fn rev(mut x: i32) -> i32 {
            let mut r = 0;
            while x > 0 {
                r = r * 10 + x % 10;
                x /= 10;
            }
            r
        }
        for i in 0..=num {
            if i + rev(i) == num {
                return true;
            }
        }
        false
    }
}

fn main() {}
