# LeetCode 1442 - Count Triplets That Can Form Two Arrays Of Equal Xor
# https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/

def count_triplets(arr)
  answer = 0
  arr.each_index do |i|
    value = 0
    (i...arr.length).each do |k|
      value ^= arr[k]
      answer += k - i if value == 0
    end
  end
  answer
end
