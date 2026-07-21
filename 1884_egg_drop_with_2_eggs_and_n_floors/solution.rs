// LeetCode 1884 - Egg Drop With 2 Eggs and N Floors
// https://leetcode.com/problems/egg-drop-with-2-eggs-and-n-floors/

impl Solution {
    pub fn two_egg_drop(n: i32) -> i32 {
        let mut moves = 0;
        let mut covered = 0;
        while covered < n {
            moves += 1;
            covered += moves;
        }
        moves
    }
}
