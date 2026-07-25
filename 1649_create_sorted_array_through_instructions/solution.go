// LeetCode 1649 - Create Sorted Array through Instructions
// https://leetcode.com/problems/create-sorted-array-through-instructions/

func createSortedArray(instructions []int) int {
	const mod = 1000000007
	mx := 0
	for _, x := range instructions {
		if x > mx {
			mx = x
		}
	}
	size := mx + 2
	bit := make([]int, size+1)
	query := func(i int) int {
		s := 0
		for i > 0 {
			s += bit[i]
			i -= i & -i
		}
		return s
	}
	update := func(j int) {
		for j <= size {
			bit[j]++
			j += j & -j
		}
	}
	ans := 0
	for i, x := range instructions {
		less := query(x - 1)
		greater := i - query(x)
		if less < greater {
			ans = (ans + less) % mod
		} else {
			ans = (ans + greater) % mod
		}
		update(x)
	}
	return ans
}
