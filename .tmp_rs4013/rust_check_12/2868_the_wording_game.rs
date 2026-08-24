struct Solution;
// LeetCode 2868 - The Wording Game
// https://leetcode.com/problems/the-wording-game/

impl Solution {
    pub fn can_alice_win(a: Vec<String>, b: Vec<String>) -> bool {
        let mut i = 0usize;
        let mut j = 0usize;
        let mut last: u8 = 0;
        let mut alice = true;
        loop {
            if alice {
                while i < a.len() && a[i].as_bytes()[0] <= last {
                    i += 1;
                }
                if i == a.len() {
                    return false;
                }
                last = *a[i].as_bytes().last().unwrap();
                i += 1;
            } else {
                while j < b.len() && b[j].as_bytes()[0] <= last {
                    j += 1;
                }
                if j == b.len() {
                    return true;
                }
                last = *b[j].as_bytes().last().unwrap();
                j += 1;
            }
            alice = !alice;
        }
    }
}

fn main() {}
