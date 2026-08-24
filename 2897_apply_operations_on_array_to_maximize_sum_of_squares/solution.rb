# LeetCode 2897 - Apply Operations on Array to Maximize Sum of Squares
# https://leetcode.com/problems/apply-operations-on-array-to-maximize-sum-of-squares/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def max_sum(nums, k)
  mod = 1_000_000_007
  cnt = Array.new(32, 0)
  nums.each do |v|
    (0...32).each { |b| cnt[b] += 1 if (v & (1 << b)) != 0 }
  end
  ans = 0
  k.times do
    cur = 0
    (0...32).each do |b|
      if cnt[b] > 0
        cur |= 1 << b
        cnt[b] -= 1
      end
    end
    ans = (ans + ((cur % mod) * (cur % mod)) % mod) % mod
  end
  ans
end
