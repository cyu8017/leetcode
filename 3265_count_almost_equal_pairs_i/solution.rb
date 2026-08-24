# LeetCode 3265 - Count Almost Equal Pairs I
# https://leetcode.com/problems/count-almost-equal-pairs-i/

# @param {Integer[]} nums
# @return {Integer}
def count_pairs(nums)
  almost_equal = lambda do |a, b|
    sa = a.to_s
    sb = b.to_s
    sa = "0" + sa while sa.length < sb.length
    sb = "0" + sb while sb.length < sa.length
    diff = []
    (0...sa.length).each { |i| diff << i if sa[i] != sb[i] }
    return true if diff.empty?
    return false if diff.length != 2
    i0 = diff[0]
    j = diff[1]
    sa[i0] == sb[j] && sa[j] == sb[i0]
  end
  ans = 0
  (0...nums.length).each do |i|
    ((i + 1)...nums.length).each { |j| ans += 1 if almost_equal.call(nums[i], nums[j]) }
  end
  ans
end
