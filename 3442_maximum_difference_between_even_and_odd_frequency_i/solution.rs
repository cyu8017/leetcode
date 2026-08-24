// LeetCode 3442 - Maximum Difference Between Even and Odd Frequency I
// https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i/

impl Solution {
    pub fn max_difference(s: String) -> i32 {
        let mut freq = [0i32; 26];
        for c in s.bytes() {
            freq[(c - b'a') as usize] += 1;
        }
        let mut max_odd = 0;
        let mut min_even = 1_000_000_000;
        for f in freq {
            if f == 0 {
                continue;
            }
            if f % 2 == 1 {
                if f > max_odd {
                    max_odd = f;
                }
            } else if f < min_even {
                min_even = f;
            }
        }
        max_odd - min_even
    }
}
