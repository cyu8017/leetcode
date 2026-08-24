// LeetCode 2621 - Sleep
// https://leetcode.com/problems/sleep/

impl Solution {
    pub fn sleep(millis: i32) {
        std::thread::sleep(std::time::Duration::from_millis(millis.max(0) as u64));
    }
}
