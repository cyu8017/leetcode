// LeetCode 3175 - Find The First Player to win K Games in a Row
// https://leetcode.com/problems/find-the-first-player-to-win-k-games-in-a-row/

impl Solution {
    pub fn find_winning_player(skills: Vec<i32>, k: i32) -> i32 {
        let n = skills.len() as i32;
        let k = k.min(n - 1);
        let mut i = 0;
        let mut cnt = 0;
        for j in 1..n {
            if skills[i as usize] < skills[j as usize] {
                i = j;
                cnt = 1;
            } else {
                cnt += 1;
            }
            if cnt == k {
                break;
            }
        }
        i
    }
}
