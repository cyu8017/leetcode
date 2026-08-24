// LeetCode 2682 - Find the Losers of the Circular Game
// https://leetcode.com/problems/find-the-losers-of-the-circular-game/

impl Solution {
    pub fn circular_game_losers(n: i32, k: i32) -> Vec<i32> {
        let mut seen = vec![0u8; (n + 1) as usize];
        let mut cur = 1;
        let mut step = 1;
        while seen[cur as usize] == 0 {
            seen[cur as usize] = 1;
            cur = (cur - 1 + step * k) % n + 1;
            step += 1;
        }
        let mut ans = Vec::new();
        for i in 1..=n {
            if seen[i as usize] == 0 {
                ans.push(i);
            }
        }
        ans
    }
}
