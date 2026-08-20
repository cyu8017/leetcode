// LeetCode 2170 - Minimum Operations to Make the Array Alternating
// https://leetcode.com/problems/minimum-operations-to-make-the-array-alternating/

func minimumOperations(nums []int) int {
	n := len(nums)
	if n == 1 {
		return 0
	}
	top2 := func(idxs []int) (int, int, int, int) {
		freq := map[int]int{}
		for _, i := range idxs {
			freq[nums[i]]++
		}
		a, ac, b, bc := 0, 0, 0, 0
		for v, c := range freq {
			if c > ac {
				b, bc = a, ac
				a, ac = v, c
			} else if c > bc {
				b, bc = v, c
			}
		}
		return a, ac, b, bc
	}
	even, odd := []int{}, []int{}
	for i := range nums {
		if i%2 == 0 {
			even = append(even, i)
		} else {
			odd = append(odd, i)
		}
	}
	e1, ec1, e2, ec2 := top2(even)
	o1, oc1, o2, oc2 := top2(odd)
	if e1 != o1 {
		return n - ec1 - oc1
	}
	a := n - ec1 - oc2
	b := n - ec2 - oc1
	if a < b {
		return a
	}
	return b
}
