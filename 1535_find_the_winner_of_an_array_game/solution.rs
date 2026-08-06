// LeetCode 1535 - Find the Winner of an Array Game
// https://leetcode.com/problems/find-the-winner-of-an-array-game/

impl Solution {
    pub fn get_winner(arr: Vec<i32>, k: i32) -> i32 {
        let mut champion = arr[0];
        let mut wins = 0;
        for &challenger in &arr[1..] {
            if champion > challenger {
                wins += 1;
            } else {
                champion = challenger;
                wins = 1;
            }
            if wins == k {
                break;
            }
        }
        champion
    }
}
