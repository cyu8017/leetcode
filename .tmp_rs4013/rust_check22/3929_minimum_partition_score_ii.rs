struct Solution;
// LeetCode 3929 - Minimum Partition Score II
// https://leetcode.com/problems/minimum-partition-score-ii/

#[derive(Clone, Copy)]
struct Line {
    slope: i64,
    intercept: i64,
    count: i32,
    valid: bool,
}

#[derive(Clone, Copy)]
struct State {
    value: i64,
    count: i32,
    valid: bool,
}

impl Default for Line {
    fn default() -> Self {
        Self {
            slope: 0,
            intercept: 0,
            count: 0,
            valid: false,
        }
    }
}

impl Default for State {
    fn default() -> Self {
        Self {
            value: 0,
            count: 0,
            valid: false,
        }
    }
}

fn better(a: State, b: State) -> State {
    if !a.valid {
        return b;
    }
    if !b.valid {
        return a;
    }
    if a.value != b.value {
        return if a.value < b.value { a } else { b };
    }
    if a.count >= b.count {
        a
    } else {
        b
    }
}

fn evaluate(line: Line, x: i64) -> State {
    if !line.valid {
        return State::default();
    }
    State {
        value: line.slope * x + line.intercept,
        count: line.count,
        valid: true,
    }
}

impl Solution {
    pub fn min_partition_score(nums: Vec<i32>, k: i32) -> i64 {
        let n = nums.len();
        let mut prefix = vec![0i64; n + 1];
        for i in 0..n {
            prefix[i + 1] = prefix[i] + nums[i] as i64;
        }

        let run = |penalty: i64| -> State {
            let mut tree = vec![Line::default(); 4 * (n + 1)];
            fn insert(
                tree: &mut [Line],
                prefix: &[i64],
                node: usize,
                left: usize,
                right: usize,
                mut line: Line,
            ) {
                if !tree[node].valid {
                    tree[node] = line;
                    return;
                }
                let mid = (left + right) / 2;
                let x_left = prefix[left];
                let x_mid = prefix[mid];
                let left_better = better(evaluate(line, x_left), evaluate(tree[node], x_left));
                let mid_better = better(evaluate(line, x_mid), evaluate(tree[node], x_mid));
                let line_wins_left =
                    left_better.value == evaluate(line, x_left).value && left_better.count == line.count;
                let line_wins_mid =
                    mid_better.value == evaluate(line, x_mid).value && mid_better.count == line.count;
                if line_wins_mid {
                    std::mem::swap(&mut tree[node], &mut line);
                }
                if left == right {
                    return;
                }
                if line_wins_left != line_wins_mid {
                    insert(tree, prefix, node * 2, left, mid, line);
                } else {
                    insert(tree, prefix, node * 2 + 1, mid + 1, right, line);
                }
            }
            fn query(
                tree: &[Line],
                prefix: &[i64],
                node: usize,
                left: usize,
                right: usize,
                index: usize,
            ) -> State {
                let result = evaluate(tree[node], prefix[index]);
                if left == right {
                    return result;
                }
                let mid = (left + right) / 2;
                if index <= mid {
                    better(result, query(tree, prefix, node * 2, left, mid, index))
                } else {
                    better(result, query(tree, prefix, node * 2 + 1, mid + 1, right, index))
                }
            }
            insert(
                &mut tree,
                &prefix,
                1,
                0,
                n,
                Line {
                    slope: 0,
                    intercept: 0,
                    count: 0,
                    valid: true,
                },
            );
            let mut current = State::default();
            for i in 1..=n {
                let best = query(&tree, &prefix, 1, 0, n, i);
                let x = prefix[i];
                current = State {
                    value: best.value + x * x + x + penalty,
                    count: best.count + 1,
                    valid: true,
                };
                insert(
                    &mut tree,
                    &prefix,
                    1,
                    0,
                    n,
                    Line {
                        slope: -2 * x,
                        intercept: current.value + x * x - x,
                        count: current.count,
                        valid: true,
                    },
                );
            }
            current
        };

        let bound = prefix[n] * prefix[n] + prefix[n] + 1;
        let mut low = 0i64;
        let mut high = bound;
        while low < high {
            let mid = low + (high - low + 1) / 2;
            if run(mid).count >= k {
                low = mid;
            } else {
                high = mid - 1;
            }
        }
        let state = run(low);
        (state.value - low * k as i64) / 2
    }
}

fn main() {}
