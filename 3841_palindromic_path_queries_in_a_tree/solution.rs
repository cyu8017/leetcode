// LeetCode 3841 - Palindromic Path Queries in a Tree
// https://leetcode.com/problems/palindromic-path-queries-in-a-tree/

impl Solution {
    pub fn palindromic_path_queries(
        n: i32,
        edges: Vec<Vec<i32>>,
        s: String,
        queries: Vec<String>,
    ) -> Vec<bool> {
        let n = n as usize;
        let mut graph = vec![Vec::new(); n];
        for e in &edges {
            let a = e[0] as usize;
            let b = e[1] as usize;
            graph[a].push(b);
            graph[b].push(a);
        }
        let mut parent = vec![-2i32; n];
        let mut depth = vec![0; n];
        parent[0] = -1;
        let mut order = vec![0];
        let mut i = 0;
        while i < order.len() {
            let u = order[i];
            for &v in &graph[u] {
                if parent[v] == -2 {
                    parent[v] = u as i32;
                    depth[v] = depth[u] + 1;
                    order.push(v);
                }
            }
            i += 1;
        }
        let mut size = vec![0; n];
        let mut heavy = vec![-1i32; n];
        for &u in order.iter().rev() {
            size[u] = 1;
            for &v in &graph[u] {
                if parent[v] == u as i32 {
                    size[u] += size[v];
                    if heavy[u] == -1 || size[v] > size[heavy[u] as usize] {
                        heavy[u] = v as i32;
                    }
                }
            }
        }
        let mut head = vec![0; n];
        let mut position = vec![0; n];
        let mut stack = vec![(0usize, 0usize)];
        let mut next_position = 0;
        while let Some((node, h)) = stack.pop() {
            let mut u = node as i32;
            while u != -1 {
                let uu = u as usize;
                head[uu] = h;
                position[uu] = next_position;
                next_position += 1;
                for &v in &graph[uu] {
                    if parent[v] == u && v as i32 != heavy[uu] {
                        stack.push((v, v));
                    }
                }
                u = heavy[uu];
            }
        }
        let mut bit = vec![0i32; n + 1];
        let update = |bit: &mut [i32], mut index: usize, value: i32| {
            index += 1;
            while index <= n {
                bit[index] ^= value;
                index += index & index.wrapping_neg();
            }
        };
        let prefix = |bit: &[i32], mut index: usize| {
            let mut result = 0;
            while index > 0 {
                result ^= bit[index];
                index -= index & index.wrapping_neg();
            }
            result
        };
        let path_mask = |bit: &[i32], mut u: usize, mut v: usize| {
            let mut result = 0;
            while head[u] != head[v] {
                if depth[head[u]] < depth[head[v]] {
                    std::mem::swap(&mut u, &mut v);
                }
                result ^= prefix(bit, position[u] + 1) ^ prefix(bit, position[head[u]]);
                u = parent[head[u]] as usize;
            }
            if position[u] > position[v] {
                std::mem::swap(&mut u, &mut v);
            }
            result ^ prefix(bit, position[v] + 1) ^ prefix(bit, position[u])
        };
        let mut current: Vec<u8> = s.into_bytes();
        for node in 0..n {
            update(&mut bit, position[node], 1 << (current[node] - b'a'));
        }
        let mut answer = Vec::new();
        for query in queries {
            let parts: Vec<&str> = query.split_whitespace().collect();
            let op = parts[0];
            let node: usize = parts[1].parse().unwrap();
            if op == "update" {
                let new_character = parts[2].as_bytes()[0];
                let delta =
                    (1 << (current[node] - b'a')) ^ (1 << (new_character - b'a'));
                update(&mut bit, position[node], delta);
                current[node] = new_character;
            } else {
                let other: usize = parts[2].parse().unwrap();
                let mask = path_mask(&bit, node, other);
                answer.push((mask & (mask - 1)) == 0);
            }
        }
        answer
    }
}
