# LeetCode 2384 - Largest Palindromic Number
# https://leetcode.com/problems/largest-palindromic-number/

# @param {String} num
# @return {String}
def largest_palindromic(num)
  freq = Array.new(10, 0)
  num.each_char { |ch| freq[ch.ord - 48] += 1 }
  left = ""
  9.downto(0) do |d|
    pairs = freq[d] / 2
    left += d.to_s * pairs
    freq[d] %= 2
  end
  mid = ""
  9.downto(0) do |d|
    if freq[d] > 0
      mid = d.to_s
      break
    end
  end
  return mid.empty? ? "0" : mid if left.empty?
  return mid.empty? ? "0" : mid if left[0] == "0"
  left + mid + left.reverse
end
