# LeetCode 3429 - Paint House IV
# https://leetcode.com/problems/paint-house-iv/

# @param {Integer} n
# @param {Integer[][]} cost
# @return {Integer}
def min_cost(n, cost)
  inf = 10**18
  m = n / 2
  dp = Array.new(3) { Array.new(3, 0) }
  (0...3).each do |a|
    (0...3).each do |b|
      dp[a][b] = a == b ? inf : cost[0][a] + cost[n - 1][b]
    end
  end
  (1...m).each do |i|
    ndp = Array.new(3) { Array.new(3, inf) }
    (0...3).each do |pa|
      (0...3).each do |pb|
        next if dp[pa][pb] >= inf

        (0...3).each do |a|
          next if a == pa

          (0...3).each do |b|
            next if b == pb || a == b

            v = dp[pa][pb] + cost[i][a] + cost[n - 1 - i][b]
            ndp[a][b] = v if v < ndp[a][b]
          end
        end
      end
    end
    dp = ndp
  end
  ans = inf
  (0...3).each do |a|
    (0...3).each do |b|
      ans = dp[a][b] if dp[a][b] < ans
    end
  end
  ans
end
