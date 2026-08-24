# LeetCode 2404 - Most Frequent Even Element
# https://leetcode.com/problems/most-frequent-even-element/

# @param {Integer[]} nums
# @return {Integer}
def most_frequent_even(nums)
  cnt = Hash.new(0)
  ans = -1
  best = 0
  nums.each do |x|
    next if x % 2 != 0
    cnt[x] += 1
    c = cnt[x]
    if c > best || (c == best && (ans == -1 || x < ans))
      best = c
      ans = x
    end
  end
  ans
end
