# LeetCode 3811 - Number of Alternating XOR Partitions
# https://leetcode.com/problems/number-of-alternating-xor-partitions/

# @param {Integer[]} nums
# @param {Integer} target1
# @param {Integer} target2
# @return {Integer}
def alternating_xor(nums, target1, target2)
  mod = 1_000_000_007
  cnt1 = Hash.new(0)
  cnt2 = Hash.new(0)
  cnt2[0] = 1
  pre = 0
  ans = 0
  nums.each do |x|
    pre ^= x
    a = cnt2[pre ^ target1]
    b = cnt1[pre ^ target2]
    ans = (a + b) % mod
    cnt1[pre] = (cnt1[pre] + a) % mod
    cnt2[pre] = (cnt2[pre] + b) % mod
  end
  ans
end
