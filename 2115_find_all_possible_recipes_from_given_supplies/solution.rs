// LeetCode 2115 - Find All Possible Recipes from Given Supplies
// https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/

use std::collections::{HashMap, HashSet, VecDeque};

impl Solution {
    pub fn find_all_recipes(
        recipes: Vec<String>,
        ingredients: Vec<Vec<String>>,
        supplies: Vec<String>,
    ) -> Vec<String> {
        let have: HashSet<String> = supplies.iter().cloned().collect();
        let mut indeg = HashMap::new();
        let mut graph: HashMap<String, Vec<String>> = HashMap::new();
        for (i, rec) in recipes.iter().enumerate() {
            indeg.insert(rec.clone(), ingredients[i].len() as i32);
            for ing in &ingredients[i] {
                graph.entry(ing.clone()).or_default().push(rec.clone());
            }
        }
        let mut q: VecDeque<String> = have.into_iter().collect();
        let mut ans = Vec::new();
        while let Some(cur) = q.pop_front() {
            if let Some(nexts) = graph.get(&cur).cloned() {
                for nxt in nexts {
                    if let Some(d) = indeg.get_mut(&nxt) {
                        *d -= 1;
                        if *d == 0 {
                            ans.push(nxt.clone());
                            q.push_back(nxt);
                        }
                    }
                }
            }
        }
        ans
    }
}
