struct Solution;

// LeetCode 2531 - Make Number of Distinct Characters Equal
// https://leetcode.com/problems/make-number-of-distinct-characters-equal/

impl Solution {
    pub fn is_it_possible(word1: String, word2: String) -> bool {
        let mut c1 = [0i32; 26];
        let mut c2 = [0i32; 26];
        for c in word1.bytes() {
            c1[(c - b'a') as usize] += 1;
        }
        for c in word2.bytes() {
            c2[(c - b'a') as usize] += 1;
        }
        let mut d1 = 0;
        let mut d2 = 0;
        for i in 0..26 {
            if c1[i] > 0 {
                d1 += 1;
            }
            if c2[i] > 0 {
                d2 += 1;
            }
        }
        for a in 0..26 {
            if c1[a] == 0 {
                continue;
            }
            for b in 0..26 {
                if c2[b] == 0 {
                    continue;
                }
                let mut nd1 = d1;
                let mut nd2 = d2;
                if a == b {
                    if nd1 == nd2 {
                        return true;
                    }
                    continue;
                }
                if c1[a] == 1 {
                    nd1 -= 1;
                }
                if c1[b] == 0 {
                    nd1 += 1;
                }
                if c2[b] == 1 {
                    nd2 -= 1;
                }
                if c2[a] == 0 {
                    nd2 += 1;
                }
                if nd1 == nd2 {
                    return true;
                }
            }
        }
        false
    }
}

fn main() {}
