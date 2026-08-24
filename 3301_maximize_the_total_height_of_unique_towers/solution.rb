# LeetCode 3301 - Maximize the Total Height of Unique Towers
# https://leetcode.com/problems/maximize-the-total-height-of-unique-towers/

# @param {Integer[]} maximum_height
# @return {Integer}
def maximum_total_sum(maximum_height)
  maximum_height.sort!.reverse!
  ans = 0
  prev = 10**18
  maximum_height.each do |h|
    cur = h
    cur = prev - 1 if cur >= prev
    return -1 if cur <= 0

    ans += cur
    prev = cur
  end
  ans
end
