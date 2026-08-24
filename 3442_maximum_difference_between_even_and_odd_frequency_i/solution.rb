# LeetCode 3442 - Maximum Difference Between Even and Odd Frequency I
# https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i/

# @param {String} s
# @return {Integer}
def max_difference(s)
  freq = Array.new(26, 0)
  s.each_char { |c| freq[c.ord - 97] += 1 }
  max_odd = 0
  min_even = 10**9
  freq.each do |f|
    next if f == 0

    if f.odd?
      max_odd = f if f > max_odd
    elsif f < min_even
      min_even = f
    end
  end
  max_odd - min_even
end
