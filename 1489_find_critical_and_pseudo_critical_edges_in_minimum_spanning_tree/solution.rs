// LeetCode 1489 - Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree
// https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/

impl Solution {
    pub fn find_critical_and_pseudo_critical_edges(n: i32, edges: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let n = n as usize;
        let mut es: Vec<(i32, usize, usize, i32)> = edges
            .iter()
            .enumerate()
            .map(|(i, e)| (e[2], e[0] as usize, e[1] as usize, i as i32))
            .collect();
        es.sort_unstable();
        let mst = |skip: Option<usize>, force: Option<usize>| -> i64 {
            let mut parent: Vec<usize> = (0..n).collect();
            fn find(parent: &mut [usize], mut x: usize) -> usize {
                while x != parent[x] {
                    parent[x] = parent[parent[x]];
                    x = parent[x];
                }
                x
            }
            let mut total = 0i64;
            let mut used = 0usize;
            if let Some(f) = force {
                let (w, a, b, _) = es[f];
                let (ra, rb) = (find(&mut parent, a), find(&mut parent, b));
                parent[ra] = rb;
                total += w as i64;
                used += 1;
            }
            for (j, &(w, a, b, _)) in es.iter().enumerate() {
                if Some(j) == skip || Some(j) == force {
                    continue;
                }
                let (x, y) = (find(&mut parent, a), find(&mut parent, b));
                if x != y {
                    parent[x] = y;
                    total += w as i64;
                    used += 1;
                }
            }
            if used == n - 1 {
                total
            } else {
                i64::MAX / 4
            }
        };
        let base = mst(None, None);
        let mut critical = Vec::new();
        let mut pseudo = Vec::new();
        for j in 0..es.len() {
            if mst(Some(j), None) > base {
                critical.push(es[j].3);
            } else if mst(None, Some(j)) == base {
                pseudo.push(es[j].3);
            }
        }
        critical.sort_unstable();
        pseudo.sort_unstable();
        vec![critical, pseudo]
    }
}
