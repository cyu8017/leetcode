// LeetCode 0278 - First Bad Version
// https://leetcode.com/problems/first-bad-version/

fn is_bad_version(version: i32) -> bool {
    let _ = version;
    false
}

impl Solution {
    pub fn first_bad_version(n: i32) -> i32 {
        let mut left = 1;
        let mut right = n;
        while left < right {
            let mid = left + (right - left) / 2;
            if is_bad_version(mid) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        left
    }
}
