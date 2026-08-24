# LeetCode 3661 - Maximum Walls Destroyed by Robots
# https://leetcode.com/problems/maximum-walls-destroyed-by-robots/

# @param {Integer[]} robots
# @param {Integer[]} distance
# @param {Integer[]} walls
# @return {Integer}
def max_walls(robots, distance, walls)
  n = robots.length
  arr = robots.zip(distance).sort_by { |a| a[0] }
  walls = walls.sort
  memo = {}
  bisect_left = lambda do |a, target|
    lo = 0
    hi = a.length
    while lo < hi
      mid = (lo + hi) >> 1
      if a[mid] < target
        lo = mid + 1
      else
        hi = mid
      end
    end
    lo
  end
  dfs = nil
  dfs = lambda do |i, j|
    return 0 if i < 0

    key = (i << 1) | j
    return memo[key] if memo.key?(key)

    left = arr[i][0] - arr[i][1]
    left = [left, arr[i - 1][0] + 1].max if i > 0
    l = bisect_left.call(walls, left)
    r = bisect_left.call(walls, arr[i][0] + 1)
    ans = dfs.call(i - 1, 0) + (r - l)
    right = arr[i][0] + arr[i][1]
    if i + 1 < arr.length
      right = if j == 0
                [right, arr[i + 1][0] - arr[i + 1][1] - 1].min
              else
                [right, arr[i + 1][0] - 1].min
              end
    end
    l = bisect_left.call(walls, arr[i][0])
    r = bisect_left.call(walls, right + 1)
    v = dfs.call(i - 1, 1) + (r - l)
    ans = v if v > ans
    memo[key] = ans
    ans
  end
  dfs.call(n - 1, 1)
end
