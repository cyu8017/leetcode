# LeetCode 3020 - Find the Maximum Number of Elements in Subset
# https://leetcode.com/problems/find-the-maximum-number-of-elements-in-subset/

# @param {Integer[]} nums
# @return {Integer}
def maximum_length(nums)
  cnt = Hash.new(0)
  nums.each { |x| cnt[x] += 1 }
  ones = cnt[1]
  ans = ones - ((ones % 2) ^ 1)
  cnt.delete(1)
  cnt.each_key do |start|
    x = start
    t = 0
    while cnt[x] > 1
      x *= x
      t += 2
    end
    if cnt[x] > 0
      t += 1
    else
      t -= 1
    end
    ans = t if t > ans
  end
  ans
end
