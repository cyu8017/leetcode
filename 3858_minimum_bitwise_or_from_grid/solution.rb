# LeetCode 3858 - Minimum Bitwise OR From Grid
# https://leetcode.com/problems/minimum-bitwise-or-from-grid/

# @param {Integer[][]} grid
# @return {Integer}
def minimum_or(grid)
  mx = 0
  grid.each { |row| row.each { |x| mx = [mx, x].max } }
  m = bit_len_3858(mx)
  ans = 0
  (m - 1).downto(0) do |i|
    mask = ans | ((1 << i) - 1)
    grid.each do |row|
      found = row.any? { |x| (x | mask) == mask }
      unless found
        ans |= 1 << i
        break
      end
    end
  end
  ans
end

def bit_len_3858(x)
  return 0 if x == 0
  n = 0
  while x > 0
    n += 1
    x >>= 1
  end
  n
end
