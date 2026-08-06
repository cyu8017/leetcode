# LeetCode 1208 - Get Equal Substrings Within Budget
# https://leetcode.com/problems/get-equal-substrings-within-budget/

# @param {String} s
# @param {String} t
# @param {Integer} max_cost
# @return {Integer}
def equal_substring(s, t, max_cost)
  left = cost = answer = 0
  s.length.times do |right|
    cost += (s[right].ord - t[right].ord).abs
    while cost > max_cost
      cost -= (s[left].ord - t[left].ord).abs
      left += 1
    end
    answer = [answer, right - left + 1].max
  end
  answer
end
