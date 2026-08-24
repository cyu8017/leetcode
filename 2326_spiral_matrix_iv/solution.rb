# LeetCode 2326 - Spiral Matrix IV
# https://leetcode.com/problems/spiral-matrix-iv/

class ListNode
  attr_accessor :val, :next

  def initialize(val = 0, nxt = nil)
    @val = val
    @next = nxt
  end
end

# @param {Integer} m
# @param {Integer} n
# @param {ListNode} head
# @return {Integer[][]}
def spiral_matrix(m, n, head)
  ans = Array.new(m) { Array.new(n, -1) }
  dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
  r = 0
  c = 0
  d = 0
  until head.nil?
    ans[r][c] = head.val
    head = head.next
    nr = r + dirs[d][0]
    nc = c + dirs[d][1]
    if nr < 0 || nr >= m || nc < 0 || nc >= n || ans[nr][nc] != -1
      d = (d + 1) % 4
      nr = r + dirs[d][0]
      nc = c + dirs[d][1]
    end
    r = nr
    c = nc
  end
  ans
end
