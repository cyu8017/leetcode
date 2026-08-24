# LeetCode 3431 - Minimum Unlocked Indices to Sort Nums
# https://leetcode.com/problems/minimum-unlocked-indices-to-sort-nums/

# @param {Integer[]} nums
# @param {Integer[]} locked
# @return {Integer}
def min_unlocked_indices(nums, locked)
  n = nums.length
  need = false
  (1...n).each do |i|
    if nums[i] < nums[i - 1]
      need = true
      break
    end
  end
  return 0 unless need

  left = n
  right = -1
  (0...n).each do |i|
    ((i + 1)...n).each do |j|
      next unless nums[i] > nums[j]

      left = i if i < left
      right = j if j > right
    end
  end
  return 0 if right < left

  ans = 0
  (left..right).each { |i| ans += 1 if locked[i] == 1 }
  tmp = nums.dup
  lock = locked.dup
  (left..right).each { |i| lock[i] = 0 }
  changed = true
  while changed
    changed = false
    (0...(n - 1)).each do |i|
      next unless lock[i] == 0 && lock[i + 1] == 0 && tmp[i] > tmp[i + 1]

      tmp[i], tmp[i + 1] = tmp[i + 1], tmp[i]
      changed = true
    end
  end
  (1...n).each { |i| return -1 if tmp[i] < tmp[i - 1] }
  ans
end
