// LeetCode 2975 - Maximum Square Area by Removing Fences From a Field
// https://leetcode.com/problems/maximum-square-area-by-removing-fences-from-a-field/

import "sort"

func maximizeSquareArea(m int, n int, hFences []int, vFences []int) int {
	const mod = 1_000_000_007
	hGaps := func(fences []int, bound int) map[int]bool {
		arr := append([]int{1}, fences...)
		arr = append(arr, bound)
		sort.Ints(arr)
		gaps := map[int]bool{}
		for i := 0; i < len(arr); i++ {
			for j := i + 1; j < len(arr); j++ {
				gaps[arr[j]-arr[i]] = true
			}
		}
		return gaps
	}
	hg := hGaps(hFences, m)
	vg := hGaps(vFences, n)
	best := -1
	for g := range hg {
		if vg[g] && g-1 > best {
			best = g - 1
		}
	}
	if best < 0 {
		return -1
	}
	return int(int64(best) * int64(best) % mod)
}
