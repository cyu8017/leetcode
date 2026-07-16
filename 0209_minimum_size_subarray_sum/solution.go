// LeetCode 0209 - Minimum Size Subarray Sum
func minSubArrayLen(target int, nums []int) int { left, total, best := 0, 0, len(nums)+1; for right, value := range nums { total += value; for total >= target { if length := right-left+1; length < best { best = length }; total -= nums[left]; left++ } }; if best == len(nums)+1 { return 0 }; return best }
