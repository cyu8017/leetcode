# LeetCode 3731 - Find Missing Elements
# https://leetcode.com/problems/find-missing-elements/

# @param {Integer[]} nums
# @return {Integer[]}
def find_missing_elements(nums)
  mn = 100
  mx = 0
  s = {}
  nums.each do |x|
    mn = [mn, x].min
    mx = [mx, x].max
    s[x] = true
  end
  ans = []
  ((mn + 1)...mx).each { |x| ans << x unless s[x] }
  ans
end
