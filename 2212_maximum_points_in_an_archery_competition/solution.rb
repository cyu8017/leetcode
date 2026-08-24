# LeetCode 2212 - Maximum Points in an Archery Competition
# https://leetcode.com/problems/maximum-points-in-an-archery-competition/

# @param {Integer} num_arrows
# @param {Integer[]} alice_arrows
# @return {Integer[]}
def maximum_bob_points(num_arrows, alice_arrows)
  best_score = -1
  best = Array.new(12, 0)
  bob = Array.new(12, 0)
  dfs = lambda do |i, remain, score|
    if i == 12
      if score > best_score
        best_score = score
        best = bob.dup
        best[0] += remain if remain > 0
      end
      return
    end
    dfs.call(i + 1, remain, score)
    need = alice_arrows[i] + 1
    if remain >= need
      bob[i] = need
      dfs.call(i + 1, remain - need, score + i)
      bob[i] = 0
    end
  end
  dfs.call(0, num_arrows, 0)
  best
end
