# LeetCode 2111 - Minimum Operations to Make the Array K-Increasing
# https://leetcode.com/problems/minimum-operations-to-make-the-array-k-increasing/

# @param {Integer[]} arr
# @param {Integer} k
# @return {Integer}
def k_increasing(arr, k)
  ans = 0
  n = arr.length
  k.times do |start|
    seq = []
    start.step(n - 1, k) { |i| seq << arr[i] }
    tails = []
    seq.each do |x|
      lo = 0
      hi = tails.length
      while lo < hi
        mid = (lo + hi) >> 1
        if tails[mid] <= x
          lo = mid + 1
        else
          hi = mid
        end
      end
      if lo == tails.length
        tails << x
      else
        tails[lo] = x
      end
    end
    ans += seq.length - tails.length
  end
  ans
end
