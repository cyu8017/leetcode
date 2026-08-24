# LeetCode 0670 - Maximum Swap
# https://leetcode.com/problems/maximum-swap/

# @param {Integer} num
# @return {Integer}
def maximum_swap(num)
  digits = num.to_s.chars
  last = {}
  digits.each_with_index { |d, i| last[d.to_i] = i }
  digits.each_with_index do |ch, i|
    9.downto(ch.to_i + 1) do |candidate|
      j = last.fetch(candidate, -1)
      if j > i
        digits[i], digits[j] = digits[j], digits[i]
        return digits.join.to_i
      end
    end
  end
  num
end
