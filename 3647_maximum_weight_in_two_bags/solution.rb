# LeetCode 3647 - Maximum Weight in Two Bags
# https://leetcode.com/problems/maximum-weight-in-two-bags/

# @param {Integer[]} weights
# @param {Integer} w1
# @param {Integer} w2
# @return {Integer}
def max_weight(weights, w1, w2)
  f = Array.new(w1 + 1) { Array.new(w2 + 1, 0) }
  weights.each do |x|
    w1.downto(0) do |j|
      w2.downto(0) do |k|
        f[j][k] = [f[j][k], f[j - x][k] + x].max if x <= j
        f[j][k] = [f[j][k], f[j][k - x] + x].max if x <= k
      end
    end
  end
  f[w1][w2]
end
