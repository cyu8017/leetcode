# LeetCode 0378 - Kth Smallest Element in a Sorted Matrix
# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

class Solution
  def kth_smallest(matrix, k)
    rows = matrix.length
    left = matrix[0][0]
    right = matrix[-1][-1]

    while left < right
      mid = (left + right) / 2
      count = 0
      column = rows - 1

      rows.times do |row|
        while column >= 0 && matrix[row][column] > mid
          column -= 1
        end
        count += column + 1
      end

      if count < k
        left = mid + 1
      else
        right = mid
      end
    end

    left
  end

  alias_method :kthSmallest, :kth_smallest
end
