package main
import "strings"
func reverseWords(s string)string{a:=strings.Fields(s);for l,r:=0,len(a)-1;l<r;l,r=l+1,r-1{a[l],a[r]=a[r],a[l]};return strings.Join(a," ")}
