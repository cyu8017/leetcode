// LeetCode 0990 - Satisfiability of Equality Equations
// https://leetcode.com/problems/satisfiability-of-equality-equations/

impl Solution {
    pub fn equations_possible(equations: Vec<String>) -> bool {
        let mut parent: Vec<usize> = (0..26).collect();
        fn find(parent: &mut [usize], x: usize) -> usize {
            if parent[x] != x {
                parent[x] = find(parent, parent[x]);
            }
            parent[x]
        }
        for eq in &equations {
            let b = eq.as_bytes();
            if b[1] == b'=' {
                let px = find(&mut parent, (b[0] - b'a') as usize);
                let py = find(&mut parent, (b[3] - b'a') as usize);
                parent[px] = py;
            }
        }
        for eq in &equations {
            let b = eq.as_bytes();
            if b[1] == b'!' {
                let px = find(&mut parent, (b[0] - b'a') as usize);
                let py = find(&mut parent, (b[3] - b'a') as usize);
                if px == py {
                    return false;
                }
            }
        }
        true
    }
}
