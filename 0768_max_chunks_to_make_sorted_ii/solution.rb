# LeetCode 0768 - Max Chunks To Make Sorted II
# https://leetcode.com/problems/max-chunks-to-make-sorted-ii/

# @param {Integer[]} arr
# @return {Integer}
def max_chunks_to_sorted(arr)
  n = arr.length
  max_left = Array.new(n, 0)
  min_right = Array.new(n, 0)
  max_left[0] = arr[0]
  (1...n).each { |i| max_left[i] = [max_left[i - 1], arr[i]].max }
  min_right[-1] = arr[-1]
  (n - 2).downto(0) { |i| min_right[i] = [min_right[i + 1], arr[i]].min }

  chunks = 1
  (0...(n - 1)).each { |i| chunks += 1 if max_left[i] <= min_right[i + 1] }
  chunks
end
