# LeetCode 0548 - Split Array with Equal Sum
# https://leetcode.com/problems/split-array-with-equal-sum/

class Solution
  def split_array(nums)
    n = nums.length
    return false if n < 7

    prefix = [0]
    nums.each do |value|
      prefix << prefix[-1] + value
    end

    (3...(n - 3)).each do |j|
      seen = {}
      (1...(j - 1)).each do |i|
        first = prefix[i] - prefix[0]
        second = prefix[j] - prefix[i + 1]
        seen[first] = true if first == second
      end

      ((j + 2)...(n - 1)).each do |k|
        third = prefix[k] - prefix[j + 1]
        fourth = prefix[n] - prefix[k + 1]
        return true if third == fourth && seen[third]
      end
    end

    false
  end

  alias_method :splitArray, :split_array
end
