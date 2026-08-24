# LeetCode 3671 - Sum of Beautiful Subsequences
# https://leetcode.com/problems/sum-of-beautiful-subsequences/

# @param {Integer[]} nums
# @return {Integer}
def total_beauty(nums)
  mod = 1_000_000_007
  mx = nums.max
  pos = Array.new(mx + 1) { [] }
  nums.each_with_index { |v, i| pos[v] << i }
  cnt = Array.new(mx + 1, 0)
  (1..mx).each do |g|
    seq = []
    g.step(mx, g) { |m| seq.concat(pos[m]) }
    next if seq.empty?

    seq.sort!
    ways = 1
    seq.length.times { ways = (ways * 2) % mod }
    cnt[g] = (ways - 1 + mod) % mod
  end
  ans = 0
  mx.downto(1) do |g|
    (2 * g).step(mx, g) { |m| cnt[g] = (cnt[g] - cnt[m] + mod) % mod }
    ans = (ans + cnt[g] * g) % mod
  end
  ans
end
