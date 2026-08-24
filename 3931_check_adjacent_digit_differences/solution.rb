# LeetCode 3931 - Check Adjacent Digit Differences
# https://leetcode.com/problems/check-adjacent-digit-differences/

# @param {String} s
# @return {Boolean}
def is_adjacent_diff_at_most_two(s)
  (1...s.length).each do |i|
    return false if (s[i - 1].ord - s[i].ord).abs > 2
  end
  true
end
