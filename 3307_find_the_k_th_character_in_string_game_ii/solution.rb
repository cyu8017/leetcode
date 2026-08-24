# LeetCode 3307 - Find the K-th Character in String Game II
# https://leetcode.com/problems/find-the-k-th-character-in-string-game-ii/

# @param {Integer} k
# @param {Integer[]} operations
# @return {Character}
def kth_character(k, operations)
  shift = 0
  ops = operations.dup
  until ops.empty?
    op = ops.pop
    half = 1 << ops.length
    if k > half
      k -= half
      shift += 1 if op == 1
    end
  end
  (97 + (shift % 26)).chr
end
