# LeetCode 2453 - Destroy Sequential Targets
# https://leetcode.com/problems/destroy-sequential-targets/

# @param {Integer[]} nums
# @param {Integer} space
# @return {Integer}
def destroy_targets(nums, space)
  cnt = Hash.new(0)
  nums.each { |x| cnt[x % space] += 1 }
  best_cnt = cnt.values.max || 0
  ans = 1_000_000_000
  cnt.each do |key, value|
    next unless value == best_cnt

    nums.each { |x| ans = x if x % space == key && x < ans }
  end
  ans
end
