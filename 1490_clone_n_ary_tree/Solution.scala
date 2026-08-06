object Solution {
  def cloneTree(root: Node): Node = {
    if (root == null) null
    else {
      val copy = new Node(root.value)
      copy.children = root.children.map(cloneTree)
      copy
    }
  }
}
