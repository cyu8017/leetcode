# LeetCode 3354 - Make Array Elements Equal to Zero
# https://leetcode.com/problems/make-array-elements-equal-to-zero/

# @param {Integer[]} nums
# @return {Integer}
def count_valid_selections(nums)
  n = nums.length
  ans = 0
  n.times do |i|
    next unless nums[i] == 0

    [-1, 1].each do |direction|
      a = nums.dup
      cur = i
      d = direction
      while cur >= 0 && cur < n
        if a[cur] == 0
          cur += d
        else
          a[cur] -= 1
          d = -d
          cur += d
        end
      end
      ans += 1 if a.all?(&:zero?)
    end
  end
  ans
end
