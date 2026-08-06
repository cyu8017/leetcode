# LeetCode 1249 - Minimum Remove to Make Valid Parentheses
# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

# @param {String} s
# @return {String}
def min_remove_to_make_valid(s)
  chars = s.chars
  opens = []
  chars.each_with_index do |ch, i|
    if ch == "("
      opens << i
    elsif ch == ")"
      if opens.empty?
        chars[i] = ""
      else
        opens.pop
      end
    end
  end
  opens.each { |i| chars[i] = "" }
  chars.join
end
