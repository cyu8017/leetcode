// LeetCode 1061 - Lexicographically Smallest Equivalent String
// https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

impl Solution {
    pub fn smallest_equivalent_string(s1: String, s2: String, base_str: String) -> String {
        let mut parent: Vec<usize> = (0..26).collect();

        fn find(parent: &mut [usize], mut x: usize) -> usize {
            while parent[x] != x {
                parent[x] = parent[parent[x]];
                x = parent[x];
            }
            x
        }

        fn union(parent: &mut [usize], a: usize, b: usize) {
            let ra = find(parent, a);
            let rb = find(parent, b);
            if ra == rb {
                return;
            }
            if ra < rb {
                parent[rb] = ra;
            } else {
                parent[ra] = rb;
            }
        }

        for (a, b) in s1.bytes().zip(s2.bytes()) {
            union(&mut parent, (a - b'a') as usize, (b - b'a') as usize);
        }
        base_str
            .bytes()
            .map(|c| (find(&mut parent, (c - b'a') as usize) as u8 + b'a') as char)
            .collect()
    }
}
