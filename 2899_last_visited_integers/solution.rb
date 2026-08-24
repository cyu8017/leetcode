# LeetCode 2899 - Last Visited Integers
# https://leetcode.com/problems/last-visited-integers/

# @param {Integer[]} nums
# @return {Integer[]}
def last_visited_integers(nums)
  seen = []
  ans = []
  k = 0
  nums.each do |v|
    if v != -1
      seen << v
      k = 0
    else
      k += 1
      ans << (k > seen.length ? -1 : seen[-k])
    end
  end
  ans
end
