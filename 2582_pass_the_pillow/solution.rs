// LeetCode 2582 - Pass the Pillow
// https://leetcode.com/problems/pass-the-pillow/

impl Solution {
    pub fn pass_the_pillow(n: i32, time: i32) -> i32 {
        let cycle = 2 * (n - 1);
        let t = time % cycle;
        if t < n {
            1 + t
        } else {
            n - (t - (n - 1))
        }
    }
}
