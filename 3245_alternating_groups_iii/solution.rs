// LeetCode 3245 - Alternating Groups III
// https://leetcode.com/problems/alternating-groups-iii/

use std::collections::BTreeSet;

struct SegTree {
    n: usize,
    tree_interval_counts: Vec<i32>,
    tree_interval_lengths: Vec<i32>,
}

impl SegTree {
    fn new(n: usize) -> Self {
        Self {
            n,
            tree_interval_counts: vec![0; 4 * n],
            tree_interval_lengths: vec![0; 4 * n],
        }
    }
    fn add(&mut self, i: i32, val: i32) {
        self.add_rec(0, 0, self.n as i32 - 1, i, val);
    }
    fn add_rec(&mut self, tree_index: usize, lo: i32, hi: i32, i: i32, val: i32) {
        if lo == hi {
            self.tree_interval_counts[tree_index] += val;
            self.tree_interval_lengths[tree_index] = self.tree_interval_counts[tree_index] * i;
            return;
        }
        let mid = (lo + hi) / 2;
        if i <= mid {
            self.add_rec(2 * tree_index + 1, lo, mid, i, val);
        } else {
            self.add_rec(2 * tree_index + 2, mid + 1, hi, i, val);
        }
        self.tree_interval_counts[tree_index] =
            self.tree_interval_counts[2 * tree_index + 1] + self.tree_interval_counts[2 * tree_index + 2];
        self.tree_interval_lengths[tree_index] =
            self.tree_interval_lengths[2 * tree_index + 1] + self.tree_interval_lengths[2 * tree_index + 2];
    }
    fn query_interval_counts(&self, i: i32) -> i32 {
        self.query(&self.tree_interval_counts, 0, 0, self.n as i32 - 1, i, self.n as i32 - 1)
    }
    fn query_interval_lengths(&self, i: i32) -> i32 {
        self.query(&self.tree_interval_lengths, 0, 0, self.n as i32 - 1, i, self.n as i32 - 1)
    }
    fn query(&self, tree: &[i32], tree_index: usize, lo: i32, hi: i32, i: i32, j: i32) -> i32 {
        if i <= lo && hi <= j {
            return tree[tree_index];
        }
        if j < lo || hi < i {
            return 0;
        }
        let mid = (lo + hi) / 2;
        self.query(tree, tree_index * 2 + 1, lo, mid, i, j)
            + self.query(tree, tree_index * 2 + 2, mid + 1, hi, i, j)
    }
}

impl Solution {
    pub fn number_of_alternating_groups(colors: Vec<i32>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let n = colors.len();
        let mut ans = Vec::new();
        let mut arr = colors.clone();
        arr.extend_from_slice(&colors[..n - 1]);
        let mut tree = SegTree::new(2 * n - 1);
        let mut intervals: BTreeSet<(i32, i32)> = BTreeSet::new();

        let insert = |intervals: &mut BTreeSet<(i32, i32)>, tree: &mut SegTree, l: i32, r: i32, n: usize| {
            intervals.insert((l, r));
            if l < n as i32 {
                tree.add(r - l + 1, 1);
            }
        };
        let remove = |intervals: &mut BTreeSet<(i32, i32)>, tree: &mut SegTree, l: i32, r: i32, n: usize| {
            intervals.remove(&(l, r));
            if l < n as i32 {
                tree.add(r - l + 1, -1);
            }
        };
        let find_interval = |intervals: &BTreeSet<(i32, i32)>, target: i32| -> (i32, i32) {
            let mut best_l = -1;
            let mut best_r = -1;
            for &(l, r) in intervals {
                if l <= target && target <= r && l > best_l {
                    best_l = l;
                    best_r = r;
                }
            }
            (best_l, best_r)
        };

        let mut start = 0i32;
        for i in 1..(2 * n - 1) as i32 {
            if arr[i as usize] == arr[(i - 1) as usize] {
                insert(&mut intervals, &mut tree, start, i - 1, n);
                start = i;
            }
        }
        insert(&mut intervals, &mut tree, start, (2 * n - 2) as i32, n);

        for query in queries {
            if query[0] == 1 {
                let sz = query[1];
                let num_intervals = tree.query_interval_counts(sz);
                let sum_intervals = tree.query_interval_lengths(sz);
                let mut num_alternating_groups = sum_intervals - num_intervals * sz + num_intervals;
                let (l, r) = find_interval(&intervals, n as i32);
                if !(l < 0 || l >= n as i32 || r - l + 1 < sz) && r >= n as i32 {
                    let non_duplicate_groups = n as i32 - l;
                    let num_groups = (r - l + 1) - sz + 1;
                    let extra = num_groups - non_duplicate_groups;
                    if extra > 0 {
                        num_alternating_groups -= extra;
                    }
                }
                ans.push(num_alternating_groups);
            } else {
                let index = query[1];
                let color = query[2];
                if arr[index as usize] != color {
                    for &idx in &[index, if index < n as i32 - 1 { index + n as i32 } else { -1 }] {
                        if idx < 0 {
                            continue;
                        }
                        if arr[idx as usize] == color {
                            continue;
                        }
                        arr[idx as usize] = color;
                        let (start, end) = find_interval(&intervals, idx);
                        remove(&mut intervals, &mut tree, start, end, n);
                        if start < idx && idx < end {
                            insert(&mut intervals, &mut tree, start, idx - 1, n);
                            insert(&mut intervals, &mut tree, idx, idx, n);
                            insert(&mut intervals, &mut tree, idx + 1, end, n);
                            continue;
                        }
                        if start == idx && idx < end {
                            insert(&mut intervals, &mut tree, start + 1, end, n);
                        }
                        if start < idx && idx == end {
                            insert(&mut intervals, &mut tree, start, end - 1, n);
                        }
                        let mut ns = idx;
                        let mut ne = idx;
                        loop {
                            let mut merged = false;
                            let keys: Vec<(i32, i32)> = intervals.iter().copied().collect();
                            for (a, b) in keys {
                                if b + 1 == ns && arr[b as usize] != arr[ns as usize] {
                                    remove(&mut intervals, &mut tree, a, b, n);
                                    ns = a;
                                    merged = true;
                                    break;
                                }
                            }
                            if !merged {
                                break;
                            }
                        }
                        loop {
                            let mut merged = false;
                            let keys: Vec<(i32, i32)> = intervals.iter().copied().collect();
                            for (a, b) in keys {
                                if a == ne + 1 && arr[a as usize] != arr[ne as usize] {
                                    remove(&mut intervals, &mut tree, a, b, n);
                                    ne = b;
                                    merged = true;
                                    break;
                                }
                            }
                            if !merged {
                                break;
                            }
                        }
                        insert(&mut intervals, &mut tree, ns, ne, n);
                    }
                }
            }
        }
        ans
    }
}
