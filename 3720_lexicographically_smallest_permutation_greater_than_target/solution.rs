// LeetCode 3720 - Lexicographically Smallest Permutation Greater Than Target
// https://leetcode.com/problems/lexicographically-smallest-permutation-greater-than-target/

impl Solution {
    pub fn lex_greater_permutation(s: String, target: String) -> String {
        let mut cnt = [0i32; 26];
        for c in s.bytes() {
            cnt[(c - b'a') as usize] += 1;
        }
        let n = s.len();
        let target = target.as_bytes();
        let mut ans = vec![b' '; n];

        fn dfs(
            pos: usize,
            greater: bool,
            n: usize,
            target: &[u8],
            cnt: &mut [i32; 26],
            ans: &mut [u8],
        ) -> bool {
            if pos == n {
                return greater;
            }
            let start = if greater { 0 } else { (target[pos] - b'a') as usize };
            for c in start..26 {
                if cnt[c] == 0 {
                    continue;
                }
                cnt[c] -= 1;
                ans[pos] = b'a' + c as u8;
                let ng = greater || c > (target[pos] - b'a') as usize;
                if dfs(pos + 1, ng, n, target, cnt, ans) {
                    return true;
                }
                cnt[c] += 1;
            }
            false
        }

        if dfs(0, false, n, target, &mut cnt, &mut ans) {
            String::from_utf8(ans).unwrap()
        } else {
            String::new()
        }
    }
}
