# LeetCode 0363 - Max Sum of Rectangle No Larger Than K
# https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/

class Solution
  def max_sum_submatrix(matrix, k)
    rows = matrix.length
    cols = rows.zero? ? 0 : matrix[0].length
    result = -Float::INFINITY

    rows.times do |top|
      col_sums = Array.new(cols, 0)
      (top...rows).each do |bottom|
        prefix_sums = [0]
        running = 0
        cols.times do |col|
          col_sums[col] += matrix[bottom][col]
          running += col_sums[col]
          index = bisect_left(prefix_sums, running - k)
          result = [result, running - prefix_sums[index]].max if index < prefix_sums.length
          insort_left(prefix_sums, running)
        end
      end
    end

    result
  end

  alias_method :maxSumSubmatrix, :max_sum_submatrix

  private

  def bisect_left(array, target)
    left = 0
    right = array.length
    while left < right
      mid = (left + right) / 2
      if array[mid] < target
        left = mid + 1
      else
        right = mid
      end
    end
    left
  end

  def insort_left(array, value)
    array.insert(bisect_left(array, value), value)
  end
end
