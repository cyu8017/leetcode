# LeetCode 0283 - Move Zeroes
# https://leetcode.com/problems/move-zeroes/

class Solution
  def moveZeroes(nums)
    insert = 0
    nums.each do |num|
      if num != 0
        nums[insert] = num
        insert += 1
      end
    end
    (insert...nums.length).each { |index| nums[index] = 0 }
  end
end
