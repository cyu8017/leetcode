// LeetCode 3335 - Total Characters in String After Transformations I
// https://leetcode.com/problems/total-characters-in-string-after-transformations-i/

impl Solution {
    pub fn length_after_transformations(s: String, t: i32) -> i32 {
        const MOD: i32 = 1_000_000_007;
        let mut cnt = [0i32; 26];
        for c in s.bytes() {
            cnt[(c - b'a') as usize] += 1;
        }
        for _ in 0..t {
            let mut ncnt = [0i32; 26];
            for i in 0..25 {
                ncnt[i + 1] = (ncnt[i + 1] + cnt[i]) % MOD;
            }
            ncnt[0] = (ncnt[0] + cnt[25]) % MOD;
            ncnt[1] = (ncnt[1] + cnt[25]) % MOD;
            cnt = ncnt;
        }
        let mut ans = 0;
        for v in cnt {
            ans = (ans + v) % MOD;
        }
        ans
    }
}
