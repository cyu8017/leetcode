# LeetCode 0060 - Permutation Sequence
# https://leetcode.com/problems/permutation-sequence/

# @param {Integer} n
# @param {Integer} k
# @return {String}
def get_permutation(n, k)
  numbers = (1..n).to_a
  factorials = [1] * n

  (1...n).each do |i|
    factorials[i] = factorials[i - 1] * i
  end

  k -= 1
  result = []

  (n - 1).downto(0) do |i|
    index = k / factorials[i]
    result << numbers[index].to_s
    numbers.delete_at(index)
    k %= factorials[i]
  end

  result.join
end
