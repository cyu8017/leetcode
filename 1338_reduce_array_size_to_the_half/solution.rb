# LeetCode 1338 - Reduce Array Size To The Half
# https://leetcode.com/problems/reduce-array-size-to-the-half/

def min_set_size(arr)
  counts = Hash.new(0)
  arr.each { |x| counts[x] += 1 }
  removed = 0
  counts.values.sort.reverse.each_with_index do |frequency, idx|
    removed += frequency
    return idx + 1 if removed * 2 >= arr.length
  end
  0
end
