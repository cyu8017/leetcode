// LeetCode 0128 - Longest Consecutive Sequence
// https://leetcode.com/problems/longest-consecutive-sequence/

func longestConsecutive(nums []int) int { values:=map[int]bool{};for _,n:=range nums{values[n]=true};best:=0;for n:=range values{if !values[n-1]{length:=1;for values[n+length]{length++};if length>best{best=length}}};return best }