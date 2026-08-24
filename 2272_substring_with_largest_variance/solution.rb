# LeetCode 2272 - Substring With Largest Variance
# https://leetcode.com/problems/substring-with-largest-variance/

# @param {String} s
# @return {Integer}
def largest_variance(s)
  ans = 0
  26.times do |ai|
    26.times do |bi|
      next if ai == bi

      a = (97 + ai).chr
      b = (97 + bi).chr
      bal = 0
      has_b = false
      s.each_char do |c|
        if c == a
          bal += 1
        elsif c == b
          bal -= 1
          has_b = true
        end
        ans = [ans, bal].max if has_b
        if bal < 0
          bal = 0
          has_b = false
        end
      end
    end
  end
  ans
end
