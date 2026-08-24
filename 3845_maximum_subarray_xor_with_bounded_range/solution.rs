// LeetCode 3845 - Maximum Subarray XOR with Bounded Range
// https://leetcode.com/problems/maximum-subarray-xor-with-bounded-range/

struct Node {
    next: [usize; 2],
    count: i32,
}

impl Solution {
    pub fn max_subarray_xor(nums: Vec<i32>, k: i32) -> i32 {
        let mut nodes = vec![Node { next: [0, 0], count: 0 }];
        fn add(nodes: &mut Vec<Node>, x: i32, delta: i32) {
            let mut u = 0;
            nodes[u].count += delta;
            for b in (0..16).rev() {
                let bit = ((x >> b) & 1) as usize;
                if nodes[u].next[bit] == 0 {
                    nodes[u].next[bit] = nodes.len();
                    nodes.push(Node { next: [0, 0], count: 0 });
                }
                u = nodes[u].next[bit];
                nodes[u].count += delta;
            }
        }
        fn query(nodes: &[Node], x: i32) -> i32 {
            let mut u = 0;
            let mut res = 0;
            for b in (0..16).rev() {
                let bit = ((x >> b) & 1) as usize;
                let want = bit ^ 1;
                let v = nodes[u].next[want];
                if v != 0 && nodes[v].count > 0 {
                    res |= 1 << b;
                    u = v;
                } else {
                    u = nodes[u].next[bit];
                }
            }
            res
        }
        let n = nums.len();
        let mut pref = vec![0; n + 1];
        for i in 0..n {
            pref[i + 1] = pref[i] ^ nums[i];
        }
        let mut max_q = Vec::new();
        let mut min_q = Vec::new();
        let mut left = 0;
        let mut trie_left = 0;
        let mut ans = 0;
        for r in 0..n {
            let x = nums[r];
            while max_q.last().map(|&i| nums[i] <= x).unwrap_or(false) {
                max_q.pop();
            }
            max_q.push(r);
            while min_q.last().map(|&i| nums[i] >= x).unwrap_or(false) {
                min_q.pop();
            }
            min_q.push(r);
            while nums[max_q[0]] - nums[min_q[0]] > k {
                if max_q[0] == left {
                    max_q.remove(0);
                }
                if min_q[0] == left {
                    min_q.remove(0);
                }
                left += 1;
            }
            add(&mut nodes, pref[r], 1);
            while trie_left < left {
                add(&mut nodes, pref[trie_left], -1);
                trie_left += 1;
            }
            let cur = query(&nodes, pref[r + 1]);
            if cur > ans {
                ans = cur;
            }
        }
        ans
    }
}
