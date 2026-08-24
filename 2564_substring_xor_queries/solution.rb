# LeetCode 2564 - Substring XOR Queries
# https://leetcode.com/problems/substring-xor-queries/

# @param {String} s
# @param {Integer[][]} queries
# @return {Integer[][]}
def substring_xor_queries(s, queries)
  pos = {}
  n = s.length
  n.times do |i|
    if s[i] == "0"
      pos[0] = [i, i] unless pos.key?(0)
      next
    end
    val = 0
    i.upto([n, i + 30].min - 1) do |j|
      val = val * 2 + (s[j].ord - 48)
      pos[val] = [i, j] unless pos.key?(val)
    end
  end
  queries.map do |a, b|
    need = a ^ b
    pos.key?(need) ? pos[need].dup : [-1, -1]
  end
end
