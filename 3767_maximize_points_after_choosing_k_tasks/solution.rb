# LeetCode 3767 - Maximize Points After Choosing K Tasks
# https://leetcode.com/problems/maximize-points-after-choosing-k-tasks/

# @param {Integer[]} technique1
# @param {Integer[]} technique2
# @param {Integer} k
# @return {Integer}
def max_points(technique1, technique2, k)
  n = technique1.length
  idx = (0...n).to_a.sort_by { |i| -(technique1[i] - technique2[i]) }
  ans = technique2.sum
  (0...k).each do |i|
    index = idx[i]
    ans -= technique2[index]
    ans += technique1[index]
  end
  (k...n).each do |i|
    index = idx[i]
    if technique1[index] >= technique2[index]
      ans -= technique2[index]
      ans += technique1[index]
    end
  end
  ans
end
