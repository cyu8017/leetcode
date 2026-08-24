# LeetCode 2171 - Removing Minimum Number of Magic Beans
# https://leetcode.com/problems/removing-minimum-number-of-magic-beans/

# @param {Integer[]} beans
# @return {Integer}
def minimum_removal(beans)
  beans = beans.sort
  n = beans.length
  sum = beans.sum
  ans = sum
  n.times do |i|
    remain = (n - i) * beans[i]
    ans = [ans, sum - remain].min
  end
  ans
end
