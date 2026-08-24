// LeetCode 2407 - Longest Increasing Subsequence II
// https://leetcode.com/problems/longest-increasing-subsequence-ii/

impl Solution {
    pub fn length_of_lis(nums: Vec<i32>, k: i32) -> i32 {
        let max_v = *nums.iter().max().unwrap() as usize;
        let mut tree = vec![0i32; 4 * (max_v + 1)];
        fn update(tree: &mut [i32], idx: usize, l: usize, r: usize, pos: usize, val: i32) {
            if l == r {
                tree[idx] = tree[idx].max(val);
                return;
            }
            let mid = (l + r) / 2;
            if pos <= mid {
                update(tree, idx * 2, l, mid, pos, val);
            } else {
                update(tree, idx * 2 + 1, mid + 1, r, pos, val);
            }
            tree[idx] = tree[idx * 2].max(tree[idx * 2 + 1]);
        }
        fn query(tree: &[i32], idx: usize, l: usize, r: usize, ql: usize, qr: usize) -> i32 {
            if qr < l || r < ql {
                return 0;
            }
            if ql <= l && r <= qr {
                return tree[idx];
            }
            let mid = (l + r) / 2;
            query(tree, idx * 2, l, mid, ql, qr).max(query(tree, idx * 2 + 1, mid + 1, r, ql, qr))
        }
        let mut ans = 0;
        for x in nums {
            let x = x as usize;
            let lo = 1.max(x.saturating_sub(k as usize));
            let mut best = 1;
            if lo <= x.saturating_sub(1) {
                best = query(&tree, 1, 1, max_v, lo, x - 1) + 1;
            }
            update(&mut tree, 1, 1, max_v, x, best);
            ans = ans.max(best);
        }
        ans
    }
}
