type TreeNode struct{Val int;Left,Right *TreeNode}
package main
func upsideDownBinaryTree(r *TreeNode)*TreeNode{var p,q *TreeNode;for r!=nil{n:=r.Left;r.Left=q;q=r.Right;r.Right=p;p=r;r=n};return p}
