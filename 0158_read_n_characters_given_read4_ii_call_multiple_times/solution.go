package main
type Solution struct{b []byte;z,i int};func Constructor()Solution{return Solution{b:make([]byte,4)}};func(s*Solution)read(b []byte,n int)int{k:=0;for k<n{if s.i==s.z{s.z=read4(s.b);s.i=0;if s.z==0{break}};for k<n&&s.i<s.z{b[k]=s.b[s.i];k++;s.i++}};return k}
