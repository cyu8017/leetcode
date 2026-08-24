# LeetCode 2094 - Finding 3-Digit Even Numbers
# https://leetcode.com/problems/finding-3-digit-even-numbers/

# @param {Integer[]} digits
# @return {Integer[]}
def find_even_numbers(digits)
  freq = Array.new(10, 0)
  digits.each { |d| freq[d] += 1 }
  ans = []
  100.step(998, 2) do |x|
    a = x / 100
    b = (x / 10) % 10
    c = x % 10
    freq[a] -= 1
    freq[b] -= 1
    freq[c] -= 1
    ans << x if freq[a] >= 0 && freq[b] >= 0 && freq[c] >= 0
    freq[a] += 1
    freq[b] += 1
    freq[c] += 1
  end
  ans
end
