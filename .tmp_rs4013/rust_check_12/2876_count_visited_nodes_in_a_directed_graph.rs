struct Solution;
// LeetCode 2876 - Count Visited Nodes in a Directed Graph
// https://leetcode.com/problems/count-visited-nodes-in-a-directed-graph/

impl Solution {
    pub fn count_visited_nodes(edges: Vec<i32>) -> Vec<i32> {
        let n = edges.len();
        let mut ans = vec![0i32; n];
        let mut state = vec![0i32; n];
        fn dfs(u: usize, edges: &[i32], ans: &mut [i32], state: &mut [i32], stack: &mut Vec<usize>) {
            state[u] = 1;
            stack.push(u);
            let v = edges[u] as usize;
            if state[v] == 0 {
                dfs(v, edges, ans, state, stack);
            } else if state[v] == 1 {
                let mut idx = stack.len() - 1;
                while stack[idx] != v {
                    idx -= 1;
                }
                let cyc = (stack.len() - idx) as i32;
                for i in idx..stack.len() {
                    ans[stack[i]] = cyc;
                }
            }
            if ans[u] == 0 {
                ans[u] = ans[edges[u] as usize] + 1;
            }
            state[u] = 2;
            stack.pop();
        }
        let mut stack = Vec::new();
        for i in 0..n {
            if state[i] == 0 {
                dfs(i, &edges, &mut ans, &mut state, &mut stack);
            }
        }
        ans
    }
}

fn main() {}
