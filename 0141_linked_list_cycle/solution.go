type ListNode struct{Val int;Next *ListNode};func hasCycle(h *ListNode)bool{for s,f:=h,h;f!=nil&&f.Next!=nil;s,f=s.Next,f.Next.Next{if s==f{return true}};return false}
