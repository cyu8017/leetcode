# LeetCode 0327 - Count of Range Sum
# https://leetcode.com/problems/count-of-range-sum/

class Solution
  def countRangeSum(nums, lower, upper)
    prefix = [0]
    nums.each { |num| prefix << prefix[-1] + num }
    temp = Array.new(prefix.length, 0)

    merge_sort = lambda do |left, right|
      return 0 if left >= right

      mid = (left + right) / 2
      count = merge_sort.call(left, mid) + merge_sort.call(mid + 1, right)
      start = mid + 1
      finish = mid + 1
      (left..mid).each do |index|
        while start <= right && prefix[start] - prefix[index] < lower
          start += 1
        end
        while finish <= right && prefix[finish] - prefix[index] <= upper
          finish += 1
        end
        count += finish - start
      end

      temp_left = left
      temp_right = mid + 1
      write = left
      while temp_left <= mid && temp_right <= right
        if prefix[temp_left] <= prefix[temp_right]
          temp[write] = prefix[temp_left]
          temp_left += 1
        else
          temp[write] = prefix[temp_right]
          temp_right += 1
        end
        write += 1
      end
      while temp_left <= mid
        temp[write] = prefix[temp_left]
        temp_left += 1
        write += 1
      end
      while temp_right <= right
        temp[write] = prefix[temp_right]
        temp_right += 1
        write += 1
      end
      (left..right).each { |i| prefix[i] = temp[i] }
      count
    end

    merge_sort.call(0, prefix.length - 1)
  end
end
