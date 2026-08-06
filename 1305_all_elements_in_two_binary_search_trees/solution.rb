# LeetCode 1305 - All Elements In Two Binary Search Trees
# https://leetcode.com/problems/all-elements-in-two-binary-search-trees/

def get_all_elements(root1, root2)
  inorder = lambda do |root|
    return [] if root.nil?
    inorder.call(root.left) + [root.val] + inorder.call(root.right)
  end
  a = inorder.call(root1)
  b = inorder.call(root2)
  answer = []
  i = 0
  j = 0
  while i < a.length || j < b.length
    if j == b.length || (i < a.length && a[i] <= b[j])
      answer << a[i]
      i += 1
    else
      answer << b[j]
      j += 1
    end
  end
  answer
end
