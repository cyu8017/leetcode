# LeetCode 2611 - Mice and Cheese
# https://leetcode.com/problems/mice-and-cheese/

# @param {Integer[]} reward1
# @param {Integer[]} reward2
# @param {Integer} k
# @return {Integer}
def mice_and_cheese(reward1, reward2, k)
  n = reward1.length
  diff = Array.new(n, 0)
  ans = 0
  n.times do |i|
    ans += reward2[i]
    diff[i] = reward1[i] - reward2[i]
  end
  diff.sort!.reverse!
  k.times { |i| ans += diff[i] }
  ans
end
