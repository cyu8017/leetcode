# LeetCode 1883 - Minimum Skips to Arrive at Meeting On Time
# https://leetcode.com/problems/minimum-skips-to-arrive-at-meeting-on-time/

# @param {Integer[]} dist
# @param {Integer} speed
# @param {Integer} hours_before
# @return {Integer}
def min_skips(dist, speed, hours_before)
  limit = hours_before * speed
  inf = 1 << 60
  dp = Array.new(dist.length + 1, inf)
  dp[0] = 0

  dist.each do |road|
    nxt = Array.new(dist.length + 1, inf)
    (0...dist.length).each do |skips|
      next if dp[skips] == inf

      nxt[skips] = [nxt[skips], ((dp[skips] + road + speed - 1) / speed) * speed].min
      nxt[skips + 1] = [nxt[skips + 1], dp[skips] + road].min
    end
    dp = nxt
  end

  dp.each_with_index do |total, skips|
    return skips if total <= limit
  end
  -1
end
