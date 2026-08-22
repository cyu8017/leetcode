// LeetCode 3595 - Once Twice
// https://leetcode.com/problems/once-twice/

func onceTwice(nums []int) []int {
	// bit counts mod 3 for each bit, then separate once vs twice
	ones := make([]int, 32)
	for _, x := range nums {
		for b := 0; b < 32; b++ {
			if (x>>b)&1 == 1 {
				ones[b]++
			}
		}
	}
	// For bits: count mod 3 is 1 if once has bit, 2 if twice has bit, 0 if neither (or both - impossible)
	once, twice := 0, 0
	for b := 0; b < 32; b++ {
		r := ones[b] % 3
		if r == 1 {
			once |= 1 << b
		} else if r == 2 {
			twice |= 1 << b
		}
	}
	// Conflict when both have same bit: r would be 0 mod 3. Need digital method.
	// Better: use two masks with ternary-like state machine per bit is hard.
	// Frequency via XOR of all with special:
	freq := map[int]int{}
	for _, x := range nums {
		freq[x]++
	}
	var a, b int
	for x, c := range freq {
		if c == 1 {
			a = x
		} else if c == 2 {
			b = x
		}
	}
	return []int{a, b}
}
