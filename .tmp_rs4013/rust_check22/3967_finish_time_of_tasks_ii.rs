struct Solution;
// LeetCode 3967 - Finish Time of Tasks II
// https://leetcode.com/problems/finish-time-of-tasks-ii/

struct Edge {
    to: usize,
    reverse: usize,
}

fn combine(minimum: i64, maximum: i64, count: i32, base: i32) -> i64 {
    if count == 0 {
        return base as i64;
    }
    2 * maximum - minimum + base as i64
}

impl Solution {
    pub fn min_finish_time(n: i32, edges: Vec<Vec<i32>>, base_time: Vec<i32>) -> i64 {
        let n = n as usize;
        let mut graph: Vec<Vec<Edge>> = (0..n).map(|_| Vec::new()).collect();
        for edge in &edges {
            let u = edge[0] as usize;
            let v = edge[1] as usize;
            let iu = graph[u].len();
            let iv = graph[v].len();
            graph[u].push(Edge { to: v, reverse: iv });
            graph[v].push(Edge { to: u, reverse: iu });
        }
        let mut parent = vec![-2i32; n];
        let mut parent_edge = vec![0usize; n];
        parent[0] = -1;
        let mut order = vec![0usize];
        let mut i = 0;
        while i < order.len() {
            let u = order[i];
            for edge in &graph[u] {
                if parent[edge.to] == -2 {
                    parent[edge.to] = u as i32;
                    parent_edge[edge.to] = edge.reverse;
                    order.push(edge.to);
                }
            }
            i += 1;
        }
        let mut incoming = vec![Vec::new(); n];
        for i in 0..n {
            incoming[i] = vec![0i64; graph[i].len()];
        }
        for oi in (1..n).rev() {
            let u = order[oi];
            let mut minimum = 1i64 << 62;
            let mut maximum = -1i64;
            let mut count = 0;
            for edge_index in 0..incoming[u].len() {
                if edge_index == parent_edge[u] {
                    continue;
                }
                let value = incoming[u][edge_index];
                minimum = minimum.min(value);
                maximum = maximum.max(value);
                count += 1;
            }
            let value = combine(minimum, maximum, count, base_time[u]);
            let parent_node = parent[u] as usize;
            let reverse_index = graph[u][parent_edge[u]].reverse;
            incoming[parent_node][reverse_index] = value;
        }
        let mut answer = 1i64 << 62;
        for &u in &order {
            let mut min1 = 1i64 << 62;
            let mut min2 = 1i64 << 62;
            let mut min_index = -1i32;
            let mut max1 = -1i64;
            let mut max2 = -1i64;
            let mut max_index = -1i32;
            for i in 0..incoming[u].len() {
                let value = incoming[u][i];
                if value < min1 {
                    min2 = min1;
                    min1 = value;
                    min_index = i as i32;
                } else if value < min2 {
                    min2 = value;
                }
                if value > max1 {
                    max2 = max1;
                    max1 = value;
                    max_index = i as i32;
                } else if value > max2 {
                    max2 = value;
                }
            }
            let root_value = combine(min1, max1, graph[u].len() as i32, base_time[u]);
            answer = answer.min(root_value);
            for i in 0..graph[u].len() {
                let edge_to = graph[u][i].to;
                let edge_reverse = graph[u][i].reverse;
                if edge_to as i32 == parent[u] {
                    continue;
                }
                if graph[u].len() == 1 {
                    incoming[edge_to][edge_reverse] = base_time[u] as i64;
                    continue;
                }
                let mut minimum = min1;
                let mut maximum = max1;
                if i as i32 == min_index {
                    minimum = min2;
                }
                if i as i32 == max_index {
                    maximum = max2;
                }
                incoming[edge_to][edge_reverse] =
                    combine(minimum, maximum, graph[u].len() as i32 - 1, base_time[u]);
            }
        }
        answer
    }
}

fn main() {}
