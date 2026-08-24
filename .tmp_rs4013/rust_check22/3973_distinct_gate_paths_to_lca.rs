struct Solution;
// LeetCode 3973 - Distinct Gate Paths to LCA
// https://leetcode.com/problems/distinct-gate-paths-to-lca/

type Mat = [[i64; 2]; 2];
const MOD: i64 = 1_000_000_007;

fn multiply(a: &Mat, b: &Mat) -> Mat {
    let mut c = [[0i64; 2]; 2];
    for i in 0..2 {
        for j in 0..2 {
            for k in 0..2 {
                c[i][j] = (c[i][j] + a[i][k] * b[k][j]) % MOD;
            }
        }
    }
    c
}

impl Solution {
    pub fn gate_path_xor(
        n: i32,
        parent: Vec<i32>,
        gates: Vec<Vec<i32>>,
        queries: Vec<Vec<i32>>,
    ) -> i32 {
        let n = n as usize;
        let mut logn = 1;
        while (1 << logn) <= n {
            logn += 1;
        }
        let mut up = vec![vec![0usize; n]; logn];
        let mut product = vec![vec![[[0i64; 2]; 2]; n]; logn];
        let mut children = vec![Vec::new(); n];
        for node in 1..n {
            children[parent[node] as usize].push(node);
        }
        let mut depth = vec![0i32; n];
        let mut order = vec![0usize];
        let mut i = 0;
        while i < order.len() {
            let u = order[i];
            for &v in &children[u] {
                depth[v] = depth[u] + 1;
                order.push(v);
            }
            i += 1;
        }
        for u in 0..n {
            up[0][u] = if u == 0 { 0 } else { parent[u] as usize };
            product[0][u] = [
                [gates[u][1] as i64, gates[u][2] as i64],
                [gates[u][2] as i64, gates[u][0] as i64],
            ];
        }
        for level in 1..logn {
            for u in 0..n {
                let mid = up[level - 1][u];
                up[level][u] = up[level - 1][mid];
                product[level][u] = multiply(&product[level - 1][u], &product[level - 1][mid]);
            }
        }
        fn lift_node(up: &[Vec<usize>], mut node: usize, mut distance: i32) -> usize {
            let mut level = 0;
            while distance > 0 {
                if distance & 1 == 1 {
                    node = up[level][node];
                }
                distance >>= 1;
                level += 1;
            }
            node
        }
        fn lca(
            up: &[Vec<usize>],
            depth: &[i32],
            logn: usize,
            mut a: usize,
            mut b: usize,
        ) -> usize {
            if depth[a] > depth[b] {
                a = lift_node(up, a, depth[a] - depth[b]);
            } else if depth[b] > depth[a] {
                b = lift_node(up, b, depth[b] - depth[a]);
            }
            if a == b {
                return a;
            }
            for level in (0..logn).rev() {
                if up[level][a] != up[level][b] {
                    a = up[level][a];
                    b = up[level][b];
                }
            }
            up[0][a]
        }
        fn ways(
            up: &[Vec<usize>],
            product: &[Vec<Mat>],
            mut node: usize,
            card: usize,
            mut distance: i32,
        ) -> i64 {
            let mut vector = [0i64; 2];
            vector[card] = 1;
            let mut level = 0;
            while distance > 0 {
                if distance & 1 == 1 {
                    let matrix = product[level][node];
                    vector = [
                        (vector[0] * matrix[0][0] + vector[1] * matrix[1][0]) % MOD,
                        (vector[0] * matrix[0][1] + vector[1] * matrix[1][1]) % MOD,
                    ];
                    node = up[level][node];
                }
                distance >>= 1;
                level += 1;
            }
            (vector[0] + vector[1]) % MOD
        }
        let mut answer = 0;
        for query in queries {
            let ancestor = lca(&up, &depth, logn, query[0] as usize, query[2] as usize);
            let alice = ways(
                &up,
                &product,
                query[0] as usize,
                query[1] as usize,
                depth[query[0] as usize] - depth[ancestor],
            );
            let bob = ways(
                &up,
                &product,
                query[2] as usize,
                query[3] as usize,
                depth[query[2] as usize] - depth[ancestor],
            );
            let total = (alice * bob % MOD) as i32;
            answer ^= total;
        }
        answer
    }
}

fn main() {}
