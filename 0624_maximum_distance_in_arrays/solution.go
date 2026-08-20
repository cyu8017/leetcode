// LeetCode 0624 - Maximum Distance in Arrays
// https://leetcode.com/problems/maximum-distance-in-arrays/

func maxDistance(arrays [][]int) int {
	minVal, maxVal := arrays[0][0], arrays[0][len(arrays[0])-1]
	best := 0
	abs := func(x int) int {
		if x < 0 {
			return -x
		}
		return x
	}
	for _, arr := range arrays[1:] {
		a := abs(arr[len(arr)-1] - minVal)
		b := abs(maxVal - arr[0])
		if a > best {
			best = a
		}
		if b > best {
			best = b
		}
		if arr[0] < minVal {
			minVal = arr[0]
		}
		if arr[len(arr)-1] > maxVal {
			maxVal = arr[len(arr)-1]
		}
	}
	return best
}
