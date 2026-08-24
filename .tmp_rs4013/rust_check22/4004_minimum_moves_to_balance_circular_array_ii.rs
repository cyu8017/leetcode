struct Solution;
// LeetCode 4004 - Minimum Moves to Balance Circular Array II
// https://leetcode.com/problems/minimum-moves-to-balance-circular-array-ii/

use std::collections::VecDeque;

const INF: i32 = 1_000_000_000;

struct Edge {
    to: usize,
    cap: i32,
    cost: i32,
    rev: usize,
}

struct MinCostMaxFlow {
    n: usize,
    graph: Vec<Vec<Edge>>,
}

impl MinCostMaxFlow {
    fn new(n: usize) -> Self {
        Self {
            n,
            graph: (0..n).map(|_| Vec::new()).collect(),
        }
    }

    fn add_edge(&mut self, u: usize, v: usize, cap: i32, cost: i32) {
        let rev_v = self.graph[v].len();
        let rev_u = self.graph[u].len();
        self.graph[u].push(Edge {
            to: v,
            cap,
            cost,
            rev: rev_v,
        });
        self.graph[v].push(Edge {
            to: u,
            cap: 0,
            cost: -cost,
            rev: rev_u,
        });
    }

    fn min_cost_flow(&mut self, source: usize, sink: usize, max_flow: i32) -> i64 {
        let mut total_cost = 0i64;
        let mut current_flow = 0;
        while current_flow < max_flow {
            let mut dist = vec![INF; self.n];
            let mut parent_node = vec![-1i32; self.n];
            let mut parent_edge = vec![-1i32; self.n];
            let mut in_queue = vec![false; self.n];
            let mut q = VecDeque::new();
            q.push_back(source);
            dist[source] = 0;
            in_queue[source] = true;
            while let Some(u) = q.pop_front() {
                in_queue[u] = false;
                for i in 0..self.graph[u].len() {
                    let e_to = self.graph[u][i].to;
                    let e_cap = self.graph[u][i].cap;
                    let e_cost = self.graph[u][i].cost;
                    if e_cap > 0 && dist[e_to] > dist[u] + e_cost {
                        dist[e_to] = dist[u] + e_cost;
                        parent_node[e_to] = u as i32;
                        parent_edge[e_to] = i as i32;
                        if !in_queue[e_to] {
                            in_queue[e_to] = true;
                            q.push_back(e_to);
                        }
                    }
                }
            }
            if dist[sink] == INF {
                return -1;
            }
            let mut push_flow = max_flow - current_flow;
            let mut cur = sink;
            while cur != source {
                let p = parent_node[cur] as usize;
                let idx = parent_edge[cur] as usize;
                if self.graph[p][idx].cap < push_flow {
                    push_flow = self.graph[p][idx].cap;
                }
                cur = p;
            }
            cur = sink;
            while cur != source {
                let p = parent_node[cur] as usize;
                let idx = parent_edge[cur] as usize;
                let rev = self.graph[p][idx].rev;
                self.graph[p][idx].cap -= push_flow;
                self.graph[cur][rev].cap += push_flow;
                cur = p;
            }
            current_flow += push_flow;
            total_cost += push_flow as i64 * dist[sink] as i64;
        }
        total_cost
    }
}

impl Solution {
    pub fn min_moves(balance: Vec<i32>) -> i64 {
        let mut total_balance = 0;
        let mut total_deficit = 0;
        for &x in &balance {
            total_balance += x;
            if x < 0 {
                total_deficit += -x;
            }
        }
        if total_balance < 0 {
            return -1;
        }
        if total_deficit == 0 {
            return 0;
        }
        let n = balance.len();
        let source = n;
        let sink = n + 1;
        let mut mcmf = MinCostMaxFlow::new(n + 2);
        for i in 0..n {
            let x = balance[i];
            if x > 0 {
                mcmf.add_edge(source, i, x, 0);
            } else if x < 0 {
                mcmf.add_edge(i, sink, -x, 0);
            }
            mcmf.add_edge(i, (i + 1) % n, INF, 1);
            mcmf.add_edge(i, (i + n - 1) % n, INF, 1);
        }
        mcmf.min_cost_flow(source, sink, total_deficit)
    }
}

fn main() {}
