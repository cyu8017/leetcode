package main
type MinStack struct{a,m []int};func Constructor()MinStack{return MinStack{}};func(s*MinStack)Push(x int){s.a=append(s.a,x);v:=x;if len(s.m)>0&&s.m[len(s.m)-1]<v{v=s.m[len(s.m)-1]};s.m=append(s.m,v)};func(s*MinStack)Pop(){s.a=s.a[:len(s.a)-1];s.m=s.m[:len(s.m)-1]};func(s*MinStack)Top()int{return s.a[len(s.a)-1]};func(s*MinStack)GetMin()int{return s.m[len(s.m)-1]}
