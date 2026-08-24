# LeetCode 3267 - Count Almost Equal Pairs II
# https://leetcode.com/problems/count-almost-equal-pairs-ii/

# @param {Integer[]} nums
# @return {Integer}
def count_pairs(nums)
  sa = sb = ""
  dfs = nil
  dfs = lambda do |arr, start, left|
    return true if arr.join == sb
    return false if left == 0
    (start...arr.length).each do |i|
      next if arr[i] == sb[i]
      ((i + 1)...arr.length).each do |j|
        next unless arr[j] == sb[i]
        arr[i], arr[j] = arr[j], arr[i]
        return true if dfs.call(arr, i + 1, left - 1)
        arr[i], arr[j] = arr[j], arr[i]
      end
      return false
    end
    arr.join == sb
  end
  almost_equal = lambda do |a, b|
    sa = a.to_s
    sb = b.to_s
    sa = "0" + sa while sa.length < sb.length
    sb = "0" + sb while sb.length < sa.length
    return true if sa == sb
    dfs.call(sa.chars, 0, 2)
  end
  ans = 0
  (0...nums.length).each do |i|
    ((i + 1)...nums.length).each { |j| ans += 1 if almost_equal.call(nums[i], nums[j]) }
  end
  ans
end
