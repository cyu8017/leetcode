type ListNode struct{Val int;Next *ListNode}
package main
func getIntersectionNode(a,b *ListNode)*ListNode{x,y:=a,b;for x!=y{if x==nil{x=b}else{x=x.Next};if y==nil{y=a}else{y=y.Next}};return x}
