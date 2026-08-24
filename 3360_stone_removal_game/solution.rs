// LeetCode 3360 - Stone Removal Game
// https://leetcode.com/problems/stone-removal-game/

impl Solution {
    pub fn can_alice_win(mut n: i32) -> bool {
        let mut take = 10;
        let mut alice = true;
        while n >= take && take > 0 {
            n -= take;
            take -= 1;
            alice = !alice;
        }
        !alice
    }
}
