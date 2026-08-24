// LeetCode 2307 - Check for Contradictions in Equations
// https://leetcode.com/problems/check-for-contradictions-in-equations/

use std::collections::HashMap;

impl Solution {
    pub fn check_contradictions(equations: Vec<Vec<String>>, values: Vec<f64>) -> bool {
        let mut parent: HashMap<String, String> = HashMap::new();
        let mut weight: HashMap<String, f64> = HashMap::new();

        fn find(
            x: &str,
            parent: &mut HashMap<String, String>,
            weight: &mut HashMap<String, f64>,
        ) -> String {
            if !parent.contains_key(x) {
                parent.insert(x.to_string(), x.to_string());
                weight.insert(x.to_string(), 1.0);
                return x.to_string();
            }
            if parent[x] != x {
                let p_name = parent[x].clone();
                let p = find(&p_name, parent, weight);
                let w = weight[&p_name];
                *weight.get_mut(x).unwrap() *= w;
                parent.insert(x.to_string(), p.clone());
                return p;
            }
            parent[x].clone()
        }

        for i in 0..equations.len() {
            let a = &equations[i][0];
            let b = &equations[i][1];
            let ra = find(a, &mut parent, &mut weight);
            let rb = find(b, &mut parent, &mut weight);
            if ra == rb {
                if (weight[a] / weight[b] - values[i]).abs() > 1e-5 {
                    return true;
                }
            } else {
                parent.insert(ra.clone(), rb);
                let wa = weight[a];
                let wb = weight[b];
                weight.insert(ra, values[i] * wb / wa);
            }
        }
        false
    }
}
