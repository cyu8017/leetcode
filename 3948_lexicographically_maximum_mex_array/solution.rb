# LeetCode 3948 - Lexicographically Maximum MEX Array
# https://leetcode.com/problems/lexicographically-maximum-mex-array/

# @param {Integer[]} nums
# @return {Integer[]}
def max_mex_array(nums)
  n = nums.length
  remaining = Array.new(n + 2, 0)
  nums.each { |x| remaining[x] += 1 if x <= n + 1 }
  mex = 0
  mex += 1 while remaining[mex] > 0
  answer = []
  seen = Array.new(n + 2, 0)
  stamp = 0
  index = 0
  while index < n
    if mex == 0
      answer << 0
      x = nums[index]
      remaining[x] -= 1 if x <= n + 1
      index += 1
      next
    end
    stamp += 1
    need = mex
    while need > 0
      x = nums[index]
      if x < mex && seen[x] != stamp
        seen[x] = stamp
        need -= 1
      end
      remaining[x] -= 1 if x <= n + 1
      index += 1
    end
    answer << mex
    mex = 0
    mex += 1 while remaining[mex] > 0
  end
  answer
end
