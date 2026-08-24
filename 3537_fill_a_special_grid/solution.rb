# LeetCode 3537 - Fill a Special Grid
# https://leetcode.com/problems/fill-a-special-grid/

# @param {Integer} n
# @return {Integer[][]}
def special_grid(n)
  m = 1 << n
  ans = Array.new(m) { Array.new(m, 0) }
  val = [0]
  dfs = nil
  dfs = lambda do |x, y, k|
    if k == 1
      ans[x][y] = val[0]
      val[0] += 1
      return
    end
    h = k >> 1
    dfs.call(x, y, h)
    dfs.call(x + h, y, h)
    dfs.call(x + h, y - h, h)
    dfs.call(x, y - h, h)
  end
  dfs.call(0, m - 1, m)
  ans
end
