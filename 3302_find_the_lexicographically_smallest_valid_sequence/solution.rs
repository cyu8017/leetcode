// LeetCode 3302 - Find the Lexicographically Smallest Valid Sequence
// https://leetcode.com/problems/find-the-lexicographically-smallest-valid-sequence/

impl Solution {
    fn can_finish(i: i32, j: i32, used_skip: bool, right: &[i32], m: i32) -> bool {
        if j >= m {
            return true;
        }
        if !used_skip {
            if right[j as usize] >= i {
                return true;
            }
            if j + 1 <= m && right[(j + 1) as usize] > i {
                return true;
            }
            if right[j as usize] > i {
                return true;
            }
            return false;
        }
        right[j as usize] >= i
    }

    pub fn valid_sequence(word1: String, word2: String) -> Vec<i32> {
        let n = word1.len() as i32;
        let m = word2.len() as i32;
        let w1 = word1.as_bytes();
        let w2 = word2.as_bytes();
        let mut right = vec![0i32; (m + 1) as usize];
        right[m as usize] = n;
        let mut j = m - 1;
        let mut i = n - 1;
        while i >= 0 && j >= 0 {
            if w1[i as usize] == w2[j as usize] {
                right[j as usize] = i;
                j -= 1;
            }
            i -= 1;
        }
        while j >= 0 {
            right[j as usize] = -1;
            j -= 1;
        }
        let mut ans = vec![0i32; m as usize];
        let mut used_skip = false;
        let mut i = 0i32;
        for j in 0..m {
            let mut found = false;
            while i < n {
                if w1[i as usize] == w2[j as usize] {
                    if Self::can_finish(i + 1, j + 1, used_skip, &right, m) {
                        ans[j as usize] = i;
                        i += 1;
                        found = true;
                        break;
                    }
                } else if !used_skip {
                    if Self::can_finish(i + 1, j + 1, true, &right, m) {
                        ans[j as usize] = i;
                        i += 1;
                        used_skip = true;
                        found = true;
                        break;
                    }
                }
                i += 1;
            }
            if !found {
                return vec![];
            }
        }
        ans
    }
}
