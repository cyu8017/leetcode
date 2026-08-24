struct Solution;
// LeetCode 0567 - Permutation in String
// https://leetcode.com/problems/permutation-in-string/

impl Solution {
    pub fn check_inclusion(s1: String, s2: String) -> bool {
        let s1: Vec<u8> = s1.into_bytes();
        let s2: Vec<u8> = s2.into_bytes();
        let n1 = s1.len();
        let n2 = s2.len();
        if n1 > n2 {
            return false;
        }
        let mut need = [0i32; 26];
        let mut window = [0i32; 26];
        for i in 0..n1 {
            need[(s1[i] - b'a') as usize] += 1;
            window[(s2[i] - b'a') as usize] += 1;
        }
        let mut matches = 0;
        for i in 0..26 {
            if need[i] == window[i] {
                matches += 1;
            }
        }
        if matches == 26 {
            return true;
        }
        for right in n1..n2 {
            let add = (s2[right] - b'a') as usize;
            let remove = (s2[right - n1] - b'a') as usize;
            if window[add] == need[add] {
                matches -= 1;
            }
            window[add] += 1;
            if window[add] == need[add] {
                matches += 1;
            }
            if window[remove] == need[remove] {
                matches -= 1;
            }
            window[remove] -= 1;
            if window[remove] == need[remove] {
                matches += 1;
            }
            if matches == 26 {
                return true;
            }
        }
        false
    }
}

fn main() {}
