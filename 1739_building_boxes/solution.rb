# LeetCode 1739 - Building Boxes
# https://leetcode.com/problems/building-boxes/

# @param {Integer} n
# @return {Integer}
def minimum_boxes(n)
  height = 0
  used = 0
  base = 0
  while used + (height + 1) * (height + 2) / 2 <= n
    height += 1
    layer = height * (height + 1) / 2
    used += layer
    base += height
  end
  extra = 0
  while used < n
    extra += 1
    used += extra
  end
  base + extra
end
