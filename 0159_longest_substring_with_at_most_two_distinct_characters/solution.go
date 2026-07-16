package main
func lengthOfLongestSubstringTwoDistinct(s string)int{m:=map[byte]int{};l,b:=0,0;for r:=range s{m[s[r]]++;for len(m)>2{m[s[l]]--;if m[s[l]]==0{delete(m,s[l])};l++};if r-l+1>b{b=r-l+1}};return b}
