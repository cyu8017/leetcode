// LeetCode 3492 - Maximum Containers on a Ship
// https://leetcode.com/problems/maximum-containers-on-a-ship/

impl Solution {
    pub fn max_containers(n: i32, w: i32, max_weight: i32) -> i32 {
        let cap = n * n;
        let by_w = max_weight / w;
        cap.min(by_w)
    }
}
