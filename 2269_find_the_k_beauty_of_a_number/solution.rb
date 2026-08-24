# LeetCode 2269 - Find the K-Beauty of a Number
# https://leetcode.com/problems/find-the-k-beauty-of-a-number/

# @param {Integer} num
# @param {Integer} k
# @return {Integer}
def divisor_substrings(num, k)
  s = num.to_s
  ans = 0
  (0..(s.length - k)).each do |i|
    sub = 0
    k.times { |j| sub = sub * 10 + (s[i + j].ord - 48) }
    ans += 1 if sub != 0 && num % sub == 0
  end
  ans
end
