# LeetCode 2243 - Calculate Digit Sum of a String
# https://leetcode.com/problems/calculate-digit-sum-of-a-string/

# @param {String} s
# @param {Integer} k
# @return {String}
def digit_sum(s, k)
  while s.length > k
    nxt = []
    i = 0
    while i < s.length
      total = 0
      end_i = [i + k, s.length].min
      (i...end_i).each { |j| total += s[j].ord - 48 }
      nxt << total.to_s
      i += k
    end
    s = nxt.join
  end
  s
end
