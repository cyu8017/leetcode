# LeetCode 2657 - Find the Prefix Common Array of Two Arrays
# https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/

# @param {Integer[]} a
# @param {Integer[]} b
# @return {Integer[]}
def find_the_prefix_common_array(a, b)
  n = a.length
  seen_a = Array.new(n + 1, false)
  seen_b = Array.new(n + 1, false)
  ans = Array.new(n, 0)
  common = 0
  n.times do |i|
    if seen_b[a[i]]
      common += 1
    end
    seen_a[a[i]] = true
    if seen_a[b[i]]
      common += 1
    end
    seen_b[b[i]] = true
    ans[i] = common
  end
  ans
end
