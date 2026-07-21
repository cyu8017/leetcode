
# @param {Integer[]} obstacles
# @return {Integer}
def min_side_jumps(obstacles)
  inf = Float::INFINITY
  dp = [1, 0, 1]

  obstacles.each do |obs|
    blocked = [obs == 1, obs == 2, obs == 3]
    ndp = [inf, inf, inf]
    3.times do |lane|
      next if blocked[lane]
      3.times do |other|
        next if blocked[other] || dp[other] == inf
        cand = dp[other] + (lane == other ? 0 : 1)
        ndp[lane] = cand if cand < ndp[lane]
      end
    end
    dp = ndp
  end

  dp.min
end
