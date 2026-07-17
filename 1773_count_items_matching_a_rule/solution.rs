// LeetCode 1773 - Count Items Matching a Rule
// https://leetcode.com/problems/count-items-matching-a-rule/

impl Solution {
    pub fn count_matches(items: Vec<Vec<String>>, rule_key: String, rule_value: String) -> i32 {
        let idx = match rule_key.as_str() {
            "type" => 0,
            "color" => 1,
            _ => 2,
        };
        items.iter().filter(|item| item[idx] == rule_value).count() as i32
    }
}
