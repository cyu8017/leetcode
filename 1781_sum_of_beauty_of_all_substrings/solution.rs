// LeetCode 1781 - Sum of Beauty of All Substrings
// https://leetcode.com/problems/sum-of-beauty-of-all-substrings/

impl Solution {
    pub fn beauty_sum(s: String) -> i32 {
        let bytes = s.as_bytes();
        let n = bytes.len();
        let mut ans = 0;
        for i in 0..n {
            let mut freq = [0i32; 26];
            for j in i..n {
                freq[(bytes[j] - b'a') as usize] += 1;
                let mut lo = i32::MAX;
                let mut hi = 0;
                for &count in freq.iter() {
                    if count > 0 {
                        lo = lo.min(count);
                        hi = hi.max(count);
                    }
                }
                ans += hi - lo;
            }
        }
        ans
    }
}
