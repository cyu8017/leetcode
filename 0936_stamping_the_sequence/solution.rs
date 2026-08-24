// LeetCode 0936 - Stamping The Sequence
// https://leetcode.com/problems/stamping-the-sequence/

impl Solution {
    pub fn moves_to_stamp(stamp: String, target: String) -> Vec<i32> {
        let n = target.len();
        let m = stamp.len();
        let stamp = stamp.as_bytes();
        let target = target.as_bytes();
        let mut done = vec![false; n];
        let mut ans = Vec::new();
        let mut changed = true;
        while changed {
            changed = false;
            for i in (0..=n.saturating_sub(m)).rev() {
                let mut ok = true;
                let mut any = false;
                for j in 0..m {
                    if !done[i + j] && target[i + j] != stamp[j] {
                        ok = false;
                        break;
                    }
                    if !done[i + j] {
                        any = true;
                    }
                }
                if ok && any {
                    for j in 0..m {
                        done[i + j] = true;
                    }
                    ans.push(i as i32);
                    changed = true;
                    break;
                }
            }
        }
        if done.iter().any(|d| !d) {
            return vec![];
        }
        ans.reverse();
        ans
    }
}
