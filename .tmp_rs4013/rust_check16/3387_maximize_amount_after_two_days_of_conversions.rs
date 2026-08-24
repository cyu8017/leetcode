struct Solution;
// LeetCode 3387 - Maximize Amount After Two Days of Conversions
// https://leetcode.com/problems/maximize-amount-after-two-days-of-conversions/

use std::collections::HashMap;

impl Solution {
    fn build_rate_graph(pairs: &[Vec<String>], rates: &[f64]) -> HashMap<String, HashMap<String, f64>> {
        let mut g: HashMap<String, HashMap<String, f64>> = HashMap::new();
        for i in 0..pairs.len() {
            let a = &pairs[i][0];
            let b = &pairs[i][1];
            g.entry(a.clone()).or_default().insert(b.clone(), rates[i]);
            g.entry(b.clone()).or_default().insert(a.clone(), 1.0 / rates[i]);
        }
        g
    }

    fn bellman(
        start: &str,
        pairs: &[Vec<String>],
        rates: &[f64],
    ) -> HashMap<String, f64> {
        let g = Self::build_rate_graph(pairs, rates);
        let mut dist = HashMap::new();
        dist.insert(start.to_string(), 1.0);
        for _ in 0..100 {
            let mut updated = false;
            for (from, edges) in &g {
                let Some(&from_d) = dist.get(from) else { continue };
                if from_d == 0.0 {
                    continue;
                }
                for (to, &rate) in edges {
                    let nv = from_d * rate;
                    if !dist.contains_key(to) || nv > dist[to] {
                        dist.insert(to.clone(), nv);
                        updated = true;
                    }
                }
            }
            if !updated {
                break;
            }
        }
        dist
    }

    pub fn max_amount(
        initial_currency: String,
        pairs1: Vec<Vec<String>>,
        rates1: Vec<f64>,
        pairs2: Vec<Vec<String>>,
        rates2: Vec<f64>,
    ) -> f64 {
        let amt1 = Self::bellman(&initial_currency, &pairs1, &rates1);
        let mut ans = 1.0;
        let g2 = Self::build_rate_graph(&pairs2, &rates2);
        for (c, &a) in &amt1 {
            if a <= 0.0 {
                continue;
            }
            let mut dist = HashMap::new();
            dist.insert(c.clone(), a);
            let mut updated = true;
            let mut it = 0;
            while it < 100 && updated {
                updated = false;
                it += 1;
                for (from, edges) in &g2 {
                    let Some(&from_d) = dist.get(from) else { continue };
                    if from_d == 0.0 {
                        continue;
                    }
                    for (to, &rate) in edges {
                        let nv = from_d * rate;
                        if !dist.contains_key(to) || nv > dist[to] {
                            dist.insert(to.clone(), nv);
                            updated = true;
                        }
                    }
                }
            }
            if let Some(&v) = dist.get(&initial_currency) {
                if v > ans {
                    ans = v;
                }
            }
        }
        ans
    }
}

fn main() {}
