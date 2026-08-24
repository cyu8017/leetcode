# LeetCode 3581 - Count Odd Letters from Number
# https://leetcode.com/problems/count-odd-letters-from-number/

# @param {Integer} n
# @return {Integer}
def count_odd_letters(n)
  d = %w[zero one two three four five six seven eight nine]
  mask = 0
  while n > 0
    d[n % 10].each_char { |c| mask ^= 1 << (c.ord - 97) }
    n /= 10
  end
  cnt = 0
  while mask != 0
    cnt += mask & 1
    mask >>= 1
  end
  cnt
end
