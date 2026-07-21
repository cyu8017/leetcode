# LeetCode 1869 - Longer Contiguous Segments of Ones than Zeros
# https://leetcode.com/problems/longer-contiguous-segments-of-ones-than-zeros/

# @param {String} s
# @return {Boolean}
def check_zero_ones(s)
  max_zeros = max_ones = 0
  zeros = ones = 0

  s.each_char do |ch|
    if ch == "0"
      zeros += 1
      ones = 0
      max_zeros = [max_zeros, zeros].max
    else
      ones += 1
      zeros = 0
      max_ones = [max_ones, ones].max
    end
  end

  max_ones > max_zeros
end
