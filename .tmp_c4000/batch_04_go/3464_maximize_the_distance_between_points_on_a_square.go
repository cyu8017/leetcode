// LeetCode 3464 - Maximize the Distance Between Points on a Square
// https://leetcode.com/problems/maximize-the-distance-between-points-on-a-square/

import "sort"

func maxDistance(side int, points [][]int, k int) int {
	// map to perimeter coordinate
	type pt struct{ d int }
	arr := make([]int, len(points))
	for i, p := range points {
		x, y := p[0], p[1]
		var d int
		if y == 0 {
			d = x
		} else if x == side {
			d = side + y
		} else if y == side {
			d = 2*side + (side - x)
		} else {
			d = 3*side + (side - y)
		}
		arr[i] = d
	}
	sort.Ints(arr)
	perim := 4 * side
	ok := func(mid int) bool {
		n := len(arr)
		for start := 0; start < n; start++ {
			cnt := 1
			last := arr[start]
			cur := start
			for cnt < k {
				need := last + mid
				found := -1
				for t := 1; t < n; t++ {
					idx := (cur + t) % n
					val := arr[idx]
					if idx <= cur {
						val += perim
					}
					if val >= need {
						found = idx
						last = arr[idx]
						if idx <= cur {
							last += perim
						}
						// normalize last into arr space for next - keep absolute
						cur = idx
						break
					}
				}
				if found == -1 {
					cnt = 0
					break
				}
				cnt++
			}
			if cnt == k {
				// check wrap distance to start
				span := last - arr[start]
				if span < 0 {
					span += perim
				}
				if perim-span >= mid || true {
					// also first-last along circle
					if minDist(arr[start], last%perim, perim) >= mid || last-arr[start] <= perim-mid {
						return true
					}
				}
			}
		}
		return false
	}
	_ = ok
	lo, hi := 0, 2*side
	for lo < hi {
		mid := (lo + hi + 1) / 2
		if canPlace(arr, perim, k, mid) {
			lo = mid
		} else {
			hi = mid - 1
		}
	}
	return lo
}

func minDist(a, b, perim int) int {
	d := a - b
	if d < 0 {
		d = -d
	}
	if perim-d < d {
		return perim - d
	}
	return d
}

func canPlace(arr []int, perim, k, mid int) bool {
	n := len(arr)
	for s := 0; s < n; s++ {
		cnt := 1
		last := arr[s]
		idx := s
		for cnt < k {
			target := last + mid
			found := false
			for step := 1; step < n; step++ {
				ni := (idx + step) % n
				val := arr[ni]
				add := 0
				if ni <= idx {
					add = perim
				}
				if val+add >= target {
					last = val + add
					idx = ni
					cnt++
					found = true
					break
				}
			}
			if !found {
				break
			}
		}
		if cnt == k && last-arr[s] <= perim-mid {
			return true
		}
	}
	return false
}
