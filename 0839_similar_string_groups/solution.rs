// LeetCode 0839 - Similar String Groups
// https://leetcode.com/problems/similar-string-groups/

impl Solution {
    pub fn num_similar_groups(strs: Vec<String>) -> i32 {
        let n = strs.len();
        let mut parent: Vec<usize> = (0..n).collect();
        fn find(parent: &mut [usize], mut x: usize) -> usize {
            while parent[x] != x {
                parent[x] = parent[parent[x]];
                x = parent[x];
            }
            x
        }
        fn similar(a: &str, b: &str) -> bool {
            let mut diff = Vec::new();
            for (i, (ca, cb)) in a.bytes().zip(b.bytes()).enumerate() {
                if ca != cb {
                    diff.push(i);
                    if diff.len() > 2 {
                        return false;
                    }
                }
            }
            diff.is_empty()
                || (diff.len() == 2
                    && a.as_bytes()[diff[0]] == b.as_bytes()[diff[1]]
                    && a.as_bytes()[diff[1]] == b.as_bytes()[diff[0]])
        }

        let mut groups = n as i32;
        for i in 0..n {
            for j in i + 1..n {
                if similar(&strs[i], &strs[j]) {
                    let pi = find(&mut parent, i);
                    let pj = find(&mut parent, j);
                    if pi != pj {
                        parent[pi] = pj;
                        groups -= 1;
                    }
                }
            }
        }
        groups
    }
}
