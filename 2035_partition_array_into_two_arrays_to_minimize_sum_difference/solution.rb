# LeetCode 2035 - Partition Array Into Two Arrays to Minimize Sum Difference
# https://leetcode.com/problems/partition-array-into-two-arrays-to-minimize-sum-difference/

# @param {Integer[]} nums
# @return {Integer}
def minimum_difference(nums)
  n = nums.length / 2
  total = nums.sum
  left = nums[0...n]
  right = nums[n..]

  sums_by_count = lambda do |arr|
    m = arr.length
    res = Array.new(m + 1) { [] }
    (0...(1 << m)).each do |mask|
      s = c = 0
      m.times do |i|
        if (mask & (1 << i)) != 0
          s += arr[i]
          c += 1
        end
      end
      res[c] << s
    end
    res.each(&:sort!)
    res
  end

  left_sums = sums_by_count.call(left)
  right_sums = sums_by_count.call(right)
  ans = 10**18
  (0..n).each do |k|
    arr = right_sums[n - k]
    left_sums[k].each do |s1|
      need = total / 2 - s1
      lo = 0
      hi = arr.length
      while lo < hi
        mid = (lo + hi) >> 1
        if arr[mid] < need
          lo = mid + 1
        else
          hi = mid
        end
      end
      [lo - 1, lo].each do |j|
        next unless j >= 0 && j < arr.length

        s2 = arr[j]
        ans = [ans, (total - 2 * (s1 + s2)).abs].min
      end
    end
  end
  ans
end
