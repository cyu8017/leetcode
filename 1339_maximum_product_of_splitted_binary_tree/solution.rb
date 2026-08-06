# LeetCode 1339 - Maximum Product Of Splitted Binary Tree
# https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/

def max_product(root)
  sums = []
  total = lambda do |node|
    return 0 if node.nil?
    value = node.val + total.call(node.left) + total.call(node.right)
    sums << value
    value
  end
  whole = total.call(root)
  sums.map { |value| value * (whole - value) }.max % 1_000_000_007
end
