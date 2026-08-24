# LeetCode 2048 - Next Greater Numerically Balanced Number
# https://leetcode.com/problems/next-greater-numerically-balanced-number/

# @param {Integer} n
# @return {Integer}
def next_beautiful_number(n)
  balanced = lambda do |x|
    cnt = Array.new(10, 0)
    while x > 0
      cnt[x % 10] += 1
      x /= 10
    end
    10.times { |d| return false if !cnt[d].zero? && cnt[d] != d }
    true
  end
  x = n + 1
  loop do
    return x if balanced.call(x)

    x += 1
  end
end
