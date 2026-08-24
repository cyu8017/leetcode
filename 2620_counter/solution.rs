// LeetCode 2620 - Counter
// https://leetcode.com/problems/counter/

impl Solution {
    pub fn create_counter(n: i32) -> impl FnMut() -> i32 {
        let mut cur = n;
        move || {
            let v = cur;
            cur += 1;
            v
        }
    }
}
