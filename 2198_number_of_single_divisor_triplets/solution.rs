// LeetCode 2198 - Number of Single Divisor Triplets
// https://leetcode.com/problems/number-of-single-divisor-triplets/

impl Solution {
    pub fn single_divisor_triplet(nums: Vec<i32>) -> i64 {
        let mut freq = [0i64; 101];
        for x in nums {
            freq[x as usize] += 1;
        }
        let mut ans = 0i64;
        for a in 1..=100 {
            if freq[a] == 0 {
                continue;
            }
            for b in a..=100 {
                if freq[b] == 0 {
                    continue;
                }
                for c in b..=100 {
                    if freq[c] == 0 {
                        continue;
                    }
                    let s = a + b + c;
                    let mut cnt = 0;
                    if s % a == 0 {
                        cnt += 1;
                    }
                    if s % b == 0 {
                        cnt += 1;
                    }
                    if s % c == 0 {
                        cnt += 1;
                    }
                    if cnt != 1 {
                        continue;
                    }
                    if a == b && b == c {
                        ans += freq[a] * (freq[a] - 1) * (freq[a] - 2);
                    } else if a == b {
                        ans += freq[a] * (freq[a] - 1) * freq[c] * 3;
                    } else if b == c {
                        ans += freq[b] * (freq[b] - 1) * freq[a] * 3;
                    } else if a == c {
                        ans += freq[a] * (freq[a] - 1) * freq[b] * 3;
                    } else {
                        ans += freq[a] * freq[b] * freq[c] * 6;
                    }
                }
            }
        }
        ans
    }
}
