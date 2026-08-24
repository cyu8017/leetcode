# LeetCode 3388 - Count Beautiful Splits in an Array
# https://leetcode.com/problems/count-beautiful-splits-in-an-array/

# @param {Integer[]} a
# @param {Integer} as_
# @param {Integer} ae
# @param {Integer[]} b
# @param {Integer} bs
# @param {Integer} be
# @return {Boolean}
def ranges_equal(a, as_, ae, b, bs, be)
  return false if ae - as_ != be - bs

  (ae - as_).times { |i| return false if a[as_ + i] != b[bs + i] }
  true
end

# @param {Integer[]} nums
# @return {Integer}
def beautiful_splits(nums)
  n = nums.length
  ans = 0
  (1...(n - 1)).each do |i|
    ((i + 1)...n).each do |j|
      ok = false
      ok = true if i <= j - i && ranges_equal(nums, 0, i, nums, i, i + i)
      ok = true if !ok && j - i <= n - j && ranges_equal(nums, i, j, nums, j, j + (j - i))
      ans += 1 if ok
    end
  end
  ans
end
