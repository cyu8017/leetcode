package main
func findMin(a []int)int{l,r:=0,len(a)-1;for l<r{m:=l+(r-l)/2;if a[m]>a[r]{l=m+1}else if a[m]<a[r]{r=m}else{r--}};return a[l]}
