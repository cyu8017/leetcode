// LeetCode 2459 - Sort Array By Moving Items to Empty Space
// https://leetcode.com/problems/sort-array-by-moving-items-to-empty-space/

func sortArray(nums []int) int {
	calc := func(target0 bool) int {
		n := len(nums)
		arr := append([]int{}, nums...)
		pos := make([]int, n)
		for i, v := range arr {
			pos[v] = i
		}
		ops := 0
		for i := 0; i < n; i++ {
			want := i
			if target0 {
				if i == 0 {
					want = 0
				} else {
					want = i
				}
			} else {
				if i == n-1 {
					want = 0
				} else {
					want = i + 1
				}
			}
			for arr[i] != want {
				empty := pos[0]
				if arr[i] == 0 {
					// swap 0 with something that belongs at empty? follow standard solution
					break
				}
				// swap current wrong value into its place via 0
				v := arr[i]
				j := pos[0]
				arr[i], arr[j] = arr[j], arr[i]
				pos[0], pos[v] = i, j
				ops++
				if arr[i] != want && arr[i] != 0 {
					// continue
				}
			}
		}
		// recompute with clearer cycle method
		return -1
	}
	_ = calc
	n := len(nums)
	solve := func(startZero bool) int {
		arr := append([]int{}, nums...)
		pos := map[int]int{}
		for i, v := range arr {
			pos[v] = i
		}
		ops := 0
		for {
			empty := pos[0]
			var should int
			if startZero {
				should = empty
			} else {
				if empty == n-1 {
					should = 0
				} else {
					should = empty + 1
				}
			}
			if arr[empty] == should {
				// find any misplaced
				found := -1
				for i := 0; i < n; i++ {
					want := i
					if !startZero {
						if i == n-1 {
							want = 0
						} else {
							want = i + 1
						}
					}
					if arr[i] != want {
						found = i
						break
					}
				}
				if found == -1 {
					return ops
				}
				v := arr[found]
				arr[empty], arr[found] = arr[found], arr[empty]
				pos[0], pos[v] = found, empty
				ops++
				continue
			}
			j := pos[should]
			v := arr[j]
			arr[empty], arr[j] = arr[j], arr[empty]
			pos[0], pos[v] = j, empty
			ops++
		}
	}
	a, b := solve(true), solve(false)
	if a < b {
		return a
	}
	return b
}
