// LeetCode 2029 - Stone Game IX
// https://leetcode.com/problems/stone-game-ix/

impl Solution {
    pub fn stone_game_ix(stones: Vec<i32>) -> bool {
        let mut cnt = [0; 3];
        for s in stones {
            cnt[(s % 3) as usize] += 1;
        }
        if cnt[0] % 2 == 0 {
            cnt[1] > 0 && cnt[2] > 0
        } else {
            (cnt[1] - cnt[2]).abs() > 2
        }
    }
}
