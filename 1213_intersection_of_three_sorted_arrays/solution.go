// LeetCode 1213 - Intersection of Three Sorted Arrays
// https://leetcode.com/problems/intersection-of-three-sorted-arrays/

func arraysIntersection(arr1 []int, arr2 []int, arr3 []int) []int {
	i, j, k := 0, 0, 0
	ans := []int{}
	for i < len(arr1) && j < len(arr2) && k < len(arr3) {
		a, b, c := arr1[i], arr2[j], arr3[k]
		if a == b && b == c {
			ans = append(ans, a)
			i++
			j++
			k++
		} else if a <= b && a <= c {
			i++
		} else if b <= a && b <= c {
			j++
		} else {
			k++
		}
	}
	return ans
}
