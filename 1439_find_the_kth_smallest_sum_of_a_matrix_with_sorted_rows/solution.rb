# LeetCode 1439 - Find The Kth Smallest Sum Of A Matrix With Sorted Rows
# https://leetcode.com/problems/find-the-kth-smallest-sum-of-a-matrix-with-sorted-rows/

def kth_smallest(mat, k)
  sums = [0]
  mat.each do |row|
    heap = [[sums[0] + row[0], 0, 0]]
    merged = []
    while !heap.empty? && merged.length < k
      heap.sort_by!(&:first)
      value, i, j = heap.shift
      merged << value
      heap << [sums[i] + row[j + 1], i, j + 1] if j + 1 < row.length
      heap << [sums[i + 1] + row[0], i + 1, 0] if j == 0 && i + 1 < sums.length
    end
    sums = merged
  end
  sums[k - 1]
end
