# LeetCode 1652 - Defuse the Bomb
# https://leetcode.com/problems/defuse-the-bomb/

# @param {Integer[]} code
# @param {Integer} k
# @return {Integer[]}
def decrypt(code, k)
  n = code.length
  return Array.new(n, 0) if k.zero?

  a = code + code
  (0...n).map do |i|
    if k.positive?
      a[(i + 1)...(i + k + 1)].sum
    else
      a[(i + n + k)...(i + n)].sum
    end
  end
end
