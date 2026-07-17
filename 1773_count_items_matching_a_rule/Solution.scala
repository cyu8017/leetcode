// LeetCode 1773 - Count Items Matching a Rule
// https://leetcode.com/problems/count-items-matching-a-rule/

object Solution {
  def countMatches(items: List[List[String]], ruleKey: String, ruleValue: String): Int = {
    val idx = ruleKey match {
      case "type"  => 0
      case "color" => 1
      case _       => 2
    }
    items.count(item => item(idx) == ruleValue)
  }
}
