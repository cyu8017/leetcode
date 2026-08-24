# LeetCode 3703 - Remove K-Balanced Substrings
# https://leetcode.com/problems/remove-k-balanced-substrings/

# @param {String} s
# @param {Integer} k
# @return {String}
def remove_substring(s, k)
  stk = []
  s.each_char do |c|
    if !stk.empty? && stk[-1][0] == c
      stk[-1][1] += 1
    else
      stk << [c, 1]
    end
    next unless c == ")" && stk.length > 1

    top = stk[-1]
    prev = stk[-2]
    if top[1] == k && prev[1] >= k
      stk.pop
      prev[1] -= k
      stk.pop if prev[1] == 0
    end
  end
  stk.map { |p| p[0] * p[1] }.join
end
