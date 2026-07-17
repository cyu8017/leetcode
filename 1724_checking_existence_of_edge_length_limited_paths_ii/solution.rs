// LeetCode 1724 - Checking Existence of Edge Length Limited Paths II
// https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths-ii/

struct DistanceLimitedPathsExist {
    weights: Vec<i32>,
    versions: Vec<Vec<usize>>,
}

impl DistanceLimitedPathsExist {
    fn new(n: i32, edge_list: Vec<Vec<i32>>) -> Self {
        let n = n as usize;
        let mut edges: Vec<(i32, usize, usize)> = edge_list
            .iter()
            .map(|edge| (edge[2], edge[0] as usize, edge[1] as usize))
            .collect();
        edges.sort_unstable();
        let mut parent: Vec<usize> = (0..n).collect();
        let mut size = vec![1usize; n];

        fn find(parent: &mut [usize], mut x: usize) -> usize {
            while parent[x] != x {
                parent[x] = parent[parent[x]];
                x = parent[x];
            }
            x
        }

        let mut weights = Vec::new();
        let mut versions = Vec::new();
        let mut i = 0;
        while i < edges.len() {
            let weight = edges[i].0;
            while i < edges.len() && edges[i].0 == weight {
                let mut ra = find(&mut parent, edges[i].1);
                let mut rb = find(&mut parent, edges[i].2);
                if ra != rb {
                    if size[ra] < size[rb] {
                        std::mem::swap(&mut ra, &mut rb);
                    }
                    parent[rb] = ra;
                    size[ra] += size[rb];
                }
                i += 1;
            }
            weights.push(weight);
            versions.push(parent.clone());
        }
        Self { weights, versions }
    }

    fn query(&self, p: i32, q: i32, limit: i32) -> bool {
        let idx = self.weights.partition_point(|&w| w < limit);
        if idx == 0 {
            return p == q;
        }
        let parent = &self.versions[idx - 1];
        let find = |mut x: usize| -> usize {
            while parent[x] != x {
                x = parent[x];
            }
            x
        };
        find(p as usize) == find(q as usize)
    }
}
