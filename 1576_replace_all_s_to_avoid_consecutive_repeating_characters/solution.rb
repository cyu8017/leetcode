# LeetCode 1576 - Replace All ?'s to Avoid Consecutive Repeating Characters
# https://leetcode.com/problems/replace-all-s-to-avoid-consecutive-repeating-characters/

# @param {String} s
# @return {String}
def modify_string(s)
  chars = s.chars
  chars.each_with_index do |ch, i|
    next unless ch == '?'
    chars[i] = %w[a b c].find do |c|
      (i.zero? || chars[i - 1] != c) && (i + 1 == chars.length || chars[i + 1] != c)
    end
  end
  chars.join
end
