// LeetCode 1871 - Jump Game VII
// https://leetcode.com/problems/jump-game-vii/

impl Solution {
    pub fn can_reach(s: String, min_jump: i32, max_jump: i32) -> bool {
        let n = s.len();
        let bytes = s.as_bytes();
        let min_jump = min_jump as usize;
        let max_jump = max_jump as usize;
        let mut reachable = vec![false; n];
        reachable[0] = true;
        let mut prefix = vec![0i32; n + 1];
        for i in 0..n {
            if i > 0 && bytes[i] == b'0' {
                let left = i.saturating_sub(max_jump);
                if i >= min_jump {
                    let right = i - min_jump;
                    if right >= left && prefix[right + 1] - prefix[left] > 0 {
                        reachable[i] = true;
                    }
                }
            }
            prefix[i + 1] = prefix[i] + if reachable[i] { 1 } else { 0 };
        }
        reachable[n - 1]
    }
}
