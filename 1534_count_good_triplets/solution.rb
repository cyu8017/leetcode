# LeetCode 1534 - Count Good Triplets
# https://leetcode.com/problems/count-good-triplets/

# @param {Integer[]} arr
# @param {Integer} a
# @param {Integer} b
# @param {Integer} c
# @return {Integer}
def count_good_triplets(arr, a, b, c)
  n = arr.length
  count = 0
  (0...n).each do |i|
    ((i + 1)...n).each do |j|
      next if (arr[i] - arr[j]).abs > a
      ((j + 1)...n).each do |k|
        count += 1 if (arr[j] - arr[k]).abs <= b && (arr[i] - arr[k]).abs <= c
      end
    end
  end
  count
end
