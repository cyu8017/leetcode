// LeetCode 3762 - Minimum Operations to Equalize Subarrays
// https://leetcode.com/problems/minimum-operations-to-equalize-subarrays/

#[derive(Clone, Copy, Default)]
struct Node {
    left: usize,
    right: usize,
    count: i32,
    sum: i64,
}

impl Solution {
    pub fn min_operations(nums: Vec<i32>, k: i32, queries: Vec<Vec<i32>>) -> Vec<i64> {
        let n = nums.len();
        let mut quotient = vec![0i32; n];
        let mut remainder = vec![0i32; n];
        let mut values = vec![0i32; n];
        for i in 0..n {
            quotient[i] = nums[i] / k;
            remainder[i] = nums[i] % k;
            values[i] = quotient[i];
        }
        values.sort_unstable();
        values.dedup();
        let mut nodes = vec![Node::default()];

        fn update(
            previous: usize,
            lo: i32,
            hi: i32,
            position: i32,
            value: i32,
            nodes: &mut Vec<Node>,
        ) -> usize {
            let current = nodes.len();
            nodes.push(nodes[previous]);
            nodes[current].count += 1;
            nodes[current].sum += value as i64;
            if lo < hi {
                let mid = (lo + hi) / 2;
                if position <= mid {
                    nodes[current].left = update(nodes[previous].left, lo, mid, position, value, nodes);
                } else {
                    nodes[current].right =
                        update(nodes[previous].right, mid + 1, hi, position, value, nodes);
                }
            }
            current
        }

        let mut roots = vec![0usize; n + 1];
        let umax = values.len() as i32 - 1;
        for i in 0..n {
            let position = values.partition_point(|&v| v < quotient[i]) as i32;
            roots[i + 1] = update(roots[i], 0, umax, position, quotient[i], &mut nodes);
        }

        fn kth(
            right_root: usize,
            left_root: usize,
            lo: i32,
            hi: i32,
            rank: i32,
            nodes: &[Node],
        ) -> i32 {
            if lo == hi {
                return lo;
            }
            let left_count = nodes[nodes[right_root].left].count - nodes[nodes[left_root].left].count;
            let mid = (lo + hi) / 2;
            if rank <= left_count {
                kth(nodes[right_root].left, nodes[left_root].left, lo, mid, rank, nodes)
            } else {
                kth(
                    nodes[right_root].right,
                    nodes[left_root].right,
                    mid + 1,
                    hi,
                    rank - left_count,
                    nodes,
                )
            }
        }

        fn prefix_stats(
            right_root: usize,
            left_root: usize,
            lo: i32,
            hi: i32,
            end: i32,
            nodes: &[Node],
        ) -> (i32, i64) {
            if end < lo {
                return (0, 0);
            }
            if hi <= end {
                return (
                    nodes[right_root].count - nodes[left_root].count,
                    nodes[right_root].sum - nodes[left_root].sum,
                );
            }
            let mid = (lo + hi) / 2;
            let (mut count, mut sum) =
                prefix_stats(nodes[right_root].left, nodes[left_root].left, lo, mid, end, nodes);
            if end > mid {
                let (c2, s2) = prefix_stats(
                    nodes[right_root].right,
                    nodes[left_root].right,
                    mid + 1,
                    hi,
                    end,
                    nodes,
                );
                count += c2;
                sum += s2;
            }
            (count, sum)
        }

        let mut logv = vec![0i32; n + 1];
        for i in 2..=n {
            logv[i] = logv[i / 2] + 1;
        }
        let levels = (logv[n] + 1) as usize;
        let mut min_table = vec![Vec::new(); levels];
        let mut max_table = vec![Vec::new(); levels];
        min_table[0] = remainder.clone();
        max_table[0] = remainder;
        for level in 1..levels {
            let length = n - (1 << level) + 1;
            min_table[level] = vec![0; length];
            max_table[level] = vec![0; length];
            let half = 1 << (level - 1);
            for i in 0..length {
                min_table[level][i] = min_table[level - 1][i].min(min_table[level - 1][i + half]);
                max_table[level][i] = max_table[level - 1][i].max(max_table[level - 1][i + half]);
            }
        }

        let mut answer = vec![0i64; queries.len()];
        for (qi, q) in queries.iter().enumerate() {
            let left = q[0] as usize;
            let right = q[1] as usize;
            let length = right - left + 1;
            let level = logv[length] as usize;
            let offset = right - (1 << level) + 1;
            let min_r = min_table[level][left].min(min_table[level][offset]);
            let max_r = max_table[level][left].max(max_table[level][offset]);
            if min_r != max_r {
                answer[qi] = -1;
                continue;
            }
            let median_index = kth(
                roots[right + 1],
                roots[left],
                0,
                umax,
                (length as i32 + 1) / 2,
                &nodes,
            );
            let median = values[median_index as usize] as i64;
            let (left_count, left_sum) =
                prefix_stats(roots[right + 1], roots[left], 0, umax, median_index, &nodes);
            let total_sum = nodes[roots[right + 1]].sum - nodes[roots[left]].sum;
            answer[qi] = median * left_count as i64 - left_sum + (total_sum - left_sum)
                - median * (length as i64 - left_count as i64);
        }
        answer
    }
}
