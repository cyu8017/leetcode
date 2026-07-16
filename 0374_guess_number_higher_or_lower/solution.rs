// LeetCode 0374 - Guess Number Higher or Lower
// https://leetcode.com/problems/guess-number-higher-or-lower/

fn guess(num: i32) -> i32 {
    let _ = num;
    0
}

impl Solution {
    pub fn guess_number(n: i32) -> i32 {
        let mut left = 1;
        let mut right = n;

        while left <= right {
            let mid = left + (right - left) / 2;
            match guess(mid) {
                0 => return mid,
                value if value < 0 => right = mid - 1,
                _ => left = mid + 1,
            }
        }

        left
    }
}
