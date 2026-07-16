package main
func maxProduct(a []int)int{b,h,l:=a[0],a[0],a[0];for _,x:=range a[1:]{oh,ol:=h,l;h=max(x,max(oh*x,ol*x));l=min(x,min(oh*x,ol*x));b=max(b,h)};return b}
func max(a,b int)int{if a>b{return a};return b};func min(a,b int)int{if a<b{return a};return b}
