struct Solution;
// LeetCode 2479 - Maximum XOR of Two Non-Overlapping Subtrees
// https://leetcode.com/problems/maximum-xor-of-two-non-overlapping-subtrees/

impl Solution {
    pub fn max_xor(n: i32, edges: Vec<Vec<i32>>, values: Vec<i32>) -> i64 {
        let n = n as usize;
        let mut g = vec![Vec::new(); n];
        for e in &edges {
            let (a, b) = (e[0] as usize, e[1] as usize);
            g[a].push(b);
            g[b].push(a);
        }
        let mut sum = vec![0i64; n];
        fn dfs_sum(u: usize, p: i32, g: &[Vec<usize>], values: &[i32], sum: &mut [i64]) -> i64 {
            let mut s = values[u] as i64;
            for &v in &g[u] {
                if v as i32 != p {
                    s += dfs_sum(v, u as i32, g, values, sum);
                }
            }
            sum[u] = s;
            s
        }
        dfs_sum(0, -1, &g, &values, &mut sum);

        struct TrieNode {
            child: [Option<Box<TrieNode>>; 2],
        }
        impl TrieNode {
            fn new() -> Self {
                Self {
                    child: [None, None],
                }
            }
        }
        let mut root = TrieNode::new();
        fn insert(root: &mut TrieNode, x: i64) {
            let mut cur = root;
            for b in (0..=46).rev() {
                let bit = ((x >> b) & 1) as usize;
                if cur.child[bit].is_none() {
                    cur.child[bit] = Some(Box::new(TrieNode::new()));
                }
                cur = cur.child[bit].as_mut().unwrap();
            }
        }
        fn query(root: &TrieNode, x: i64) -> i64 {
            if root.child[0].is_none() && root.child[1].is_none() {
                return 0;
            }
            let mut cur = root;
            let mut ans = 0i64;
            for b in (0..=46).rev() {
                let bit = ((x >> b) & 1) as usize;
                let want = bit ^ 1;
                if cur.child[want].is_some() {
                    ans |= 1i64 << b;
                    cur = cur.child[want].as_ref().unwrap();
                } else if cur.child[bit].is_some() {
                    cur = cur.child[bit].as_ref().unwrap();
                } else {
                    return ans;
                }
            }
            ans
        }

        let mut ans = 0i64;
        fn dfs(
            u: usize,
            p: i32,
            g: &[Vec<usize>],
            sum: &[i64],
            root: &mut TrieNode,
            ans: &mut i64,
        ) {
            for &v in &g[u] {
                if v as i32 == p {
                    continue;
                }
                let xorv = query(root, sum[v]);
                if xorv > *ans {
                    *ans = xorv;
                }
                dfs(v, u as i32, g, sum, root, ans);
                insert(root, sum[v]);
            }
        }
        dfs(0, -1, &g, &sum, &mut root, &mut ans);
        ans
    }
}

fn main() {}
