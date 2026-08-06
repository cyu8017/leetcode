# LeetCode 1430 - Check If A String Is A Valid Sequence From Root To Leaves Path In A Binary Tree
# https://leetcode.com/problems/check-if-a-string-is-a-valid-sequence-from-root-to-leaves-path-in-a-binary-tree/

def is_valid_sequence(root, arr)
  visit = lambda do |node, index|
    return false if node.nil? || index == arr.length || node.val != arr[index]
    return index == arr.length - 1 if node.left.nil? && node.right.nil?
    visit.call(node.left, index + 1) || visit.call(node.right, index + 1)
  end
  visit.call(root, 0)
end
