struct Solution;
// LeetCode 3327 - Check if DFS Strings Are Palindromes
// https://leetcode.com/problems/check-if-dfs-strings-are-palindromes/

impl Solution {
    fn is_pal(s: &str) -> bool {
        let b = s.as_bytes();
        let mut i = 0;
        let mut j = b.len() as i32 - 1;
        while i < j {
            if b[i as usize] != b[j as usize] {
                return false;
            }
            i += 1;
            j -= 1;
        }
        true
    }

    pub fn find_answer(parent: Vec<i32>, s: String) -> Vec<bool> {
        let n = parent.len();
        let mut g = vec![Vec::new(); n];
        for i in 1..n {
            g[parent[i] as usize].push(i);
        }
        let sb = s.as_bytes();
        let mut ans = vec![false; n];
        fn dfs_str(u: usize, g: &[Vec<usize>], sb: &[u8], ans: &mut [bool]) -> String {
            let mut out = String::new();
            for &v in &g[u] {
                out.push_str(&dfs_str(v, g, sb, ans));
            }
            out.push(sb[u] as char);
            ans[u] = Solution::is_pal(&out);
            out
        }
        dfs_str(0, &g, sb, &mut ans);
        ans
    }
}

fn main() {}
