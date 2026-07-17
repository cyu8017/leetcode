# LeetCode 1773 - Count Items Matching a Rule
# https://leetcode.com/problems/count-items-matching-a-rule/

# @param {String[][]} items
# @param {String} rule_key
# @param {String} rule_value
# @return {Integer}
def count_matches(items, rule_key, rule_value)
  idx = { 'type' => 0, 'color' => 1, 'name' => 2 }[rule_key]
  items.count { |item| item[idx] == rule_value }
end
