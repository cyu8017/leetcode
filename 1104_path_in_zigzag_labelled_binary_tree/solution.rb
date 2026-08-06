# LeetCode 1104 - Path In Zigzag Labelled Binary Tree
# https://leetcode.com/problems/path-in-zigzag-labelled-binary-tree/

# @param {Integer} label
# @return {Integer[]}
def path_in_zig_zag_tree(label)
  path = [label]
  while label > 1
    level = label.bit_length - 1
    label >>= 1
    label = (1 << level) - 1 - label + (1 << (level - 1))
    path << label
  end
  path.reverse
end
