# LeetCode 1522 - Diameter of N-Ary Tree
# https://leetcode.com/problems/diameter-of-n-ary-tree/

# @param {Node} root
# @return {Integer}
def diameter(root)
  answer = 0
  depth = lambda do |node|
    longest = second = 0
    node.children.each do |child|
      value = depth.call(child) + 1
      if value > longest
        longest, second = value, longest
      elsif value > second
        second = value
      end
    end
    answer = [answer, longest + second].max
    longest
  end
  depth.call(root) if root
  answer
end
