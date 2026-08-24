# LeetCode 3725 - Count Ways to Choose Coprime Integers from Rows
# https://leetcode.com/problems/count-ways-to-choose-coprime-integers-from-rows/

# @param {Integer[][]} mat
# @return {Integer}
def count_coprime(mat)
  mod = 1_000_000_007
  m = mat.length
  dp = Hash.new(0)
  mat[0].each { |v| dp[v] += 1 }
  (1...m).each do |i|
    ndp = Hash.new(0)
    mat[i].each do |v|
      dp.each do |key, val|
        ng = key.gcd(v)
        ndp[ng] = (ndp[ng] + val) % mod
      end
    end
    dp = ndp
  end
  dp[1]
end
