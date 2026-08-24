# LeetCode 3681 - Maximum XOR of Subsequences
# https://leetcode.com/problems/maximum-xor-of-subsequences/

# @param {Integer[]} nums
# @return {Integer}
def max_xor_subsequences(nums)
  basis = Array.new(32, 0)
  nums.each do |x|
    cur = x
    31.downto(0) do |b|
      next if (cur & (1 << b)) == 0

      if basis[b] == 0
        basis[b] = cur
        break
      end
      cur ^= basis[b]
    end
  end
  ans = 0
  31.downto(0) { |b| ans ^= basis[b] if (ans ^ basis[b]) > ans }
  ans
end
