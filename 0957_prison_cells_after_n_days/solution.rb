# LeetCode 0957 - Prison Cells After N Days
# https://leetcode.com/problems/prison-cells-after-n-days/

# @param {Integer[]} cells
# @param {Integer} n
# @return {Integer[]}
def prison_after_n_days(cells, n)
  seen = {}
  state = cells.dup
  while n > 0
    key = state.join(",")
    if seen.key?(key)
      cycle = seen[key] - n
      n %= cycle
      break if n == 0
    end
    seen[key] = n
    nxt = [0] + (1..6).map { |i| state[i - 1] == state[i + 1] ? 1 : 0 } + [0]
    state = nxt
    n -= 1
  end
  state
end
