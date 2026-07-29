# LeetCode 1088 - Confusing Number II
# https://leetcode.com/problems/confusing-number-ii/

# @param {Integer} n
# @return {Integer}
def confusing_number_ii(n)
  rotate = { 0 => 0, 1 => 1, 6 => 9, 8 => 8, 9 => 6 }
  digits = [0, 1, 6, 8, 9]
  ans = 0

  is_confusing = lambda do |num|
    original = num
    rotated = 0
    while num.positive?
      d = num % 10
      rotated = rotated * 10 + rotate[d]
      num /= 10
    end
    rotated != original
  end

  dfs = lambda do |cur|
    return if cur > n

    ans += 1 if cur.positive? && is_confusing.call(cur)
    if cur.zero?
      [1, 6, 8, 9].each { |d| dfs.call(d) }
    else
      digits.each { |d| dfs.call(cur * 10 + d) }
    end
  end

  dfs.call(0)
  ans
end
