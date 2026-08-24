# LeetCode 0769 - Max Chunks To Make Sorted
# https://leetcode.com/problems/max-chunks-to-make-sorted/

# @param {Integer[]} arr
# @return {Integer}
def max_chunks_to_sorted(arr)
  chunks = 0
  max_so_far = 0
  arr.each_with_index do |value, i|
    max_so_far = [max_so_far, value].max
    chunks += 1 if max_so_far == i
  end
  chunks
end
