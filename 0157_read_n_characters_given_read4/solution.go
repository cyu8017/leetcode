package main
func read(b []byte,n int)int{k:=0;t:=make([]byte,4);for k<n{c:=read4(t);if c==0{break};for i:=0;i<c&&k<n;i++{b[k]=t[i];k++}};return k}
