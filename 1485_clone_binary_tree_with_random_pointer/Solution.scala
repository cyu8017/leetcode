object Solution {
  def copyRandomBinaryTree(root: Node): Node = {
    val copies = scala.collection.mutable.HashMap.empty[Node, Node]
    def cloneNode(node: Node): Node = {
      if (node == null) null
      else copies.get(node) match {
        case Some(copy) => copy
        case None =>
        val copy = new Node(node.value)
        copies(node) = copy
        copy.left = cloneNode(node.left)
        copy.right = cloneNode(node.right)
        copy.random = cloneNode(node.random)
        copy
      }
    }
    cloneNode(root)
  }
}
