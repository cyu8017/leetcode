# LeetCode 1066 - Campus Bikes II
# https://leetcode.com/problems/campus-bikes-ii/

# @param {Integer[][]} workers
# @param {Integer[][]} bikes
# @return {Integer}
def assign_bikes(workers, bikes)
  m = bikes.length
  memo = {}

  dp = lambda do |i, mask|
    return 0 if i == workers.length

    key = [i, mask]
    return memo[key] if memo.key?(key)

    best = Float::INFINITY
    wx, wy = workers[i]
    m.times do |b|
      next if (mask & (1 << b)) != 0

      bx, by = bikes[b]
      dist = (wx - bx).abs + (wy - by).abs
      best = [best, dist + dp.call(i + 1, mask | (1 << b))].min
    end
    memo[key] = best
  end

  dp.call(0, 0)
end
