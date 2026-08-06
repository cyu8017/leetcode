// LeetCode 1268 - Search Suggestions System
// https://leetcode.com/problems/search-suggestions-system/

impl Solution {
    pub fn suggested_products(mut products: Vec<String>, search_word: String) -> Vec<Vec<String>> {
        products.sort();
        let mut ans = Vec::new();
        let mut prefix = String::new();
        for ch in search_word.chars() {
            prefix.push(ch);
            let idx = products.partition_point(|p| p.as_str() < prefix.as_str());
            let mut group = Vec::new();
            for j in idx..products.len().min(idx + 3) {
                if products[j].starts_with(&prefix) {
                    group.push(products[j].clone());
                }
            }
            ans.push(group);
        }
        ans
    }
}
