# LeetCode 0956 - Tallest Billboard
# https://leetcode.com/problems/tallest-billboard/

# @param {Integer[]} rods
# @return {Integer}
def tallest_billboard(rods)
  dp = { 0 => 0 }
  rods.each do |rod|
    dp.to_a.each do |diff, taller|
      dp[diff + rod] = [dp.fetch(diff + rod, 0), taller + rod].max
      nd = (diff - rod).abs
      nxt = diff >= rod ? taller : taller - diff + rod
      dp[nd] = [dp.fetch(nd, 0), nxt].max
    end
  end
  dp.fetch(0, 0)
end
