# LeetCode 2151 - Maximum Good People Based on Statements
# https://leetcode.com/problems/maximum-good-people-based-on-statements/

# @param {Integer[][]} statements
# @return {Integer}
def maximum_good(statements)
  n = statements.length
  ok = lambda do |mask|
    n.times do |i|
      next if (mask & (1 << i)).zero?

      n.times do |j|
        s = statements[i][j]
        next if s == 2

        good_j = (mask & (1 << j)) != 0
        return false if (s == 1 && !good_j) || (s == 0 && good_j)
      end
    end
    true
  end

  ans = 0
  (1 << n).times do |mask|
    next unless ok.call(mask)

    bc = 0
    x = mask
    while x > 0
      bc += x & 1
      x >>= 1
    end
    ans = [ans, bc].max
  end
  ans
end
