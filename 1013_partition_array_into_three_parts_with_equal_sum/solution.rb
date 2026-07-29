# LeetCode 1013 - Partition Array Into Three Parts With Equal Sum
# https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/

# @param {Integer[]} arr
# @return {Boolean}
def can_three_parts_equal_sum(arr)
  total = arr.sum
  return false if total % 3 != 0

  target = total / 3
  parts = cur = 0
  arr.each do |x|
    cur += x
    if cur == target
      parts += 1
      cur = 0
    end
  end
  parts >= 3
end
