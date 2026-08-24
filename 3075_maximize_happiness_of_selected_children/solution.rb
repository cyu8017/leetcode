# LeetCode 3075 - Maximize Happiness of Selected Children
# https://leetcode.com/problems/maximize-happiness-of-selected-children/

# @param {Integer[]} happiness
# @param {Integer} k
# @return {Integer}
def maximum_happiness_sum(happiness, k)
  happiness.sort!
  ans = 0
  k.times do |i|
    x = happiness[happiness.length - i - 1] - i
    ans += [x, 0].max
  end
  ans
end
