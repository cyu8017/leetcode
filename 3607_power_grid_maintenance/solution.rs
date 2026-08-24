// LeetCode 3607 - Power Grid Maintenance
// https://leetcode.com/problems/power-grid-maintenance/

use std::collections::HashMap;

impl Solution {
    pub fn process_queries(c: i32, connections: Vec<Vec<i32>>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let c = c as usize;
        let mut parent: Vec<usize> = (0..=c).collect();
        fn find(parent: &mut [usize], x: usize) -> usize {
            if parent[x] != x {
                parent[x] = find(parent, parent[x]);
            }
            parent[x]
        }
        let unite = |parent: &mut [usize], a: usize, b: usize| {
            let ra = find(parent, a);
            let rb = find(parent, b);
            if ra != rb {
                if ra < rb {
                    parent[rb] = ra;
                } else {
                    parent[ra] = rb;
                }
            }
        };
        for e in &connections {
            unite(&mut parent, e[0] as usize, e[1] as usize);
        }
        let mut online = vec![true; c + 1];
        let mut comp: HashMap<usize, Vec<usize>> = HashMap::new();
        for i in 1..=c {
            let r = find(&mut parent, i);
            comp.entry(r).or_default().push(i);
        }
        for ids in comp.values_mut() {
            ids.sort();
        }
        let mut ptr: HashMap<usize, usize> = HashMap::new();
        let mut ans = Vec::new();
        for q in queries {
            let (t, x) = (q[0], q[1] as usize);
            if t == 2 {
                online[x] = false;
                continue;
            }
            if online[x] {
                ans.push(x as i32);
                continue;
            }
            let r = find(&mut parent, x);
            let ids = &comp[&r];
            let p = ptr.entry(r).or_insert(0);
            while *p < ids.len() && !online[ids[*p]] {
                *p += 1;
            }
            ans.push(if *p < ids.len() { ids[*p] as i32 } else { -1 });
        }
        ans
    }
}
