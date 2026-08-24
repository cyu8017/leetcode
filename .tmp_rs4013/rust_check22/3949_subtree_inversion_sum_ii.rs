struct Solution;
// LeetCode 3949 - Subtree Inversion Sum II
// https://leetcode.com/problems/subtree-inversion-sum-ii/

impl Solution {
    pub fn max_subtree_inversion_sum(edges: Vec<Vec<i32>>, nums: Vec<i32>, k: i32) -> i64 {
        let n = nums.len();
        let k = k as usize;
        let mut graph = vec![Vec::new(); n];
        for edge in &edges {
            graph[edge[0] as usize].push(edge[1] as usize);
            graph[edge[1] as usize].push(edge[0] as usize);
        }
        let mut parent = vec![-2i32; n];
        parent[0] = -1;
        let mut order = vec![0usize];
        let mut i = 0;
        while i < order.len() {
            let u = order[i];
            for &v in &graph[u] {
                if parent[v] == -2 {
                    parent[v] = u as i32;
                    order.push(v);
                }
            }
            i += 1;
        }
        const INFINITY: i64 = 1 << 60;
        let mut maximum = vec![Vec::new(); n];
        let mut minimum = vec![Vec::new(); n];
        for &u in order.iter().rev() {
            let mut current_max = vec![-INFINITY; k + 1];
            let mut current_min = vec![INFINITY; k + 1];
            current_max[k] = nums[u] as i64;
            current_min[k] = nums[u] as i64;
            for &v in &graph[u] {
                if parent[v] != u as i32 {
                    continue;
                }
                let mut next_max = vec![-INFINITY; k + 1];
                let mut next_min = vec![INFINITY; k + 1];
                for first in 0..=k {
                    if current_max[first] == -INFINITY {
                        continue;
                    }
                    for child_distance in 0..=k {
                        if maximum[v][child_distance] == -INFINITY {
                            continue;
                        }
                        let mut second = child_distance + 1;
                        if second > k {
                            second = k;
                        }
                        if first < k && second < k && first + second < k {
                            continue;
                        }
                        let distance = first.min(second);
                        let max_value = current_max[first] + maximum[v][child_distance];
                        let min_value = current_min[first] + minimum[v][child_distance];
                        next_max[distance] = next_max[distance].max(max_value);
                        next_min[distance] = next_min[distance].min(min_value);
                    }
                }
                current_max = next_max;
                current_min = next_min;
            }
            if -current_min[k] > current_max[0] {
                current_max[0] = -current_min[k];
            }
            if -current_max[k] < current_min[0] {
                current_min[0] = -current_max[k];
            }
            maximum[u] = current_max;
            minimum[u] = current_min;
        }
        let mut answer = -(1i64 << 60);
        for &value in &maximum[0] {
            answer = answer.max(value);
        }
        answer
    }
}

fn main() {}
