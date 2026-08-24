# LeetCode 3612 - Process String with Special Operations I
# https://leetcode.com/problems/process-string-with-special-operations-i/

# @param {String} s
# @return {String}
def process_str(s)
  result = []
  s.each_char do |c|
    if c =~ /[a-zA-Z]/
      result << c
    elsif c == "*"
      result.pop unless result.empty?
    elsif c == "#"
      result += result
    elsif c == "%"
      result.reverse!
    end
  end
  result.join
end
