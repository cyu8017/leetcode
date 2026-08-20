// LeetCode 0969 - Pancake Sorting
// https://leetcode.com/problems/pancake-sorting/

func pancakeSort(arr []int) []int {
	a := append([]int{}, arr...)
	ans := []int{}
	for size := len(a); size > 1; size-- {
		i := 0
		for j, v := range a {
			if v == size {
				i = j
				break
			}
		}
		if i == size-1 {
			continue
		}
		if i > 0 {
			ans = append(ans, i+1)
			for l, r := 0, i; l < r; l, r = l+1, r-1 {
				a[l], a[r] = a[r], a[l]
			}
		}
		ans = append(ans, size)
		for l, r := 0, size-1; l < r; l, r = l+1, r-1 {
			a[l], a[r] = a[r], a[l]
		}
	}
	return ans
}
