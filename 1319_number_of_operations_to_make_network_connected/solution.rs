// LeetCode 1319 - Number of Operations to Make Network Connected
// https://leetcode.com/problems/number-of-operations-to-make-network-connected/

impl Solution {
    pub fn make_connected(n: i32, connections: Vec<Vec<i32>>) -> i32 {
        let n = n as usize;
        if connections.len() < n - 1 {
            return -1;
        }
        let mut parent: Vec<usize> = (0..n).collect();
        fn find(parent: &mut [usize], mut x: usize) -> usize {
            while x != parent[x] {
                parent[x] = parent[parent[x]];
                x = parent[x];
            }
            x
        }
        for e in connections {
            let (a, b) = (e[0] as usize, e[1] as usize);
            let (ra, rb) = (find(&mut parent, a), find(&mut parent, b));
            if ra != rb {
                parent[ra] = rb;
            }
        }
        let mut roots = std::collections::HashSet::new();
        for i in 0..n {
            roots.insert(find(&mut parent, i));
        }
        (roots.len() as i32) - 1
    }
}
