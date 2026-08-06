// LeetCode 1938 - Maximum Genetic Difference Query
// https://leetcode.com/problems/maximum-genetic-difference-query/

struct TrieNode {
    child: [Option<Box<TrieNode>>; 2],
    cnt: i32,
}

impl TrieNode {
    fn new() -> Self {
        Self {
            child: [None, None],
            cnt: 0,
        }
    }
}

impl Solution {
    pub fn max_genetic_difference(parents: Vec<i32>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let n = parents.len();
        let mut children = vec![Vec::new(); n];
        let mut root = 0usize;
        for (i, &p) in parents.iter().enumerate() {
            if p == -1 {
                root = i;
            } else {
                children[p as usize].push(i);
            }
        }

        let mut qmap = vec![Vec::new(); n];
        for (i, q) in queries.iter().enumerate() {
            qmap[q[0] as usize].push((i, q[1]));
        }

        let mut ans = vec![0; queries.len()];
        let mut trie = TrieNode::new();
        const BITS: i32 = 17;

        fn trie_update(trie: &mut TrieNode, num: i32, delta: i32) {
            let mut node = trie;
            for b in (0..=BITS).rev() {
                let bit = ((num >> b) & 1) as usize;
                if node.child[bit].is_none() {
                    node.child[bit] = Some(Box::new(TrieNode::new()));
                }
                node = node.child[bit].as_mut().unwrap();
                node.cnt += delta;
            }
        }

        fn trie_max_xor(trie: &TrieNode, num: i32) -> i32 {
            let mut node = trie;
            let mut res = 0;
            for b in (0..=BITS).rev() {
                let bit = ((num >> b) & 1) as usize;
                let want = 1 - bit;
                if node.child[want]
                    .as_ref()
                    .map(|c| c.cnt > 0)
                    .unwrap_or(false)
                {
                    res |= 1 << b;
                    node = node.child[want].as_ref().unwrap();
                } else {
                    node = node.child[bit].as_ref().unwrap();
                }
            }
            res
        }

        fn dfs(
            u: usize,
            children: &[Vec<usize>],
            qmap: &[Vec<(usize, i32)>],
            trie: &mut TrieNode,
            ans: &mut [i32],
        ) {
            trie_update(trie, u as i32, 1);
            for &(qi, val) in &qmap[u] {
                ans[qi] = trie_max_xor(trie, val);
            }
            for &v in &children[u] {
                dfs(v, children, qmap, trie, ans);
            }
            trie_update(trie, u as i32, -1);
        }

        dfs(root, &children, &qmap, &mut trie, &mut ans);
        ans
    }
}
