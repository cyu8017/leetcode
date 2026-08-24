// LeetCode 3579 - Minimum Steps to Convert String with Operations
// https://leetcode.com/problems/minimum-steps-to-convert-string-with-operations/

impl Solution {
    pub fn min_operations(word1: String, word2: String) -> i32 {
        let n = word1.len();
        let w1 = word1.as_bytes();
        let w2 = word2.as_bytes();
        let mut f = vec![i32::MAX / 2; n + 1];
        f[0] = 0;
        let calc = |l: usize, r: usize, rev: bool| -> i32 {
            let mut cnt = [[0i32; 26]; 26];
            let mut res = 0;
            for i in l..=r {
                let j = if rev { r - (i - l) } else { i };
                let a = (w1[j] - b'a') as usize;
                let b = (w2[i] - b'a') as usize;
                if a != b {
                    if cnt[b][a] > 0 {
                        cnt[b][a] -= 1;
                    } else {
                        cnt[a][b] += 1;
                        res += 1;
                    }
                }
            }
            res
        };
        for i in 1..=n {
            for j in 0..i {
                let a = calc(j, i - 1, false);
                let b = 1 + calc(j, i - 1, true);
                f[i] = f[i].min(f[j] + a.min(b));
            }
        }
        f[n]
    }
}
