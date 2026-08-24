# LeetCode 3507 - Minimum Pair Removal to Sort Array I
# https://leetcode.com/problems/minimum-pair-removal-to-sort-array-i/

# @param {Integer[]} nums
# @return {Integer}
def minimum_pair_removal(nums)
  is_non_decreasing = lambda do |a|
    (1...a.length).each { |i| return false if a[i] < a[i - 1] }
    true
  end
  arr = nums.dup
  ans = 0
  until is_non_decreasing.call(arr)
    k = 0
    s = arr[0] + arr[1]
    (1...(arr.length - 1)).each do |i|
      t = arr[i] + arr[i + 1]
      if s > t
        s = t
        k = i
      end
    end
    arr[k] = s
    arr.delete_at(k + 1)
    ans += 1
  end
  ans
end
