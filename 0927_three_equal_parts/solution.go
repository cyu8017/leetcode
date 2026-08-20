// LeetCode 0927 - Three Equal Parts
// https://leetcode.com/problems/three-equal-parts/

func threeEqualParts(arr []int) []int {
	ones := []int{}
	for i, bit := range arr {
		if bit == 1 {
			ones = append(ones, i)
		}
	}
	n := len(ones)
	if n%3 != 0 {
		return []int{-1, -1}
	}
	if n == 0 {
		return []int{0, len(arr) - 1}
	}
	third := n / 3
	length := ones[n-1] - ones[2*third] + 1
	a, b, c := ones[0], ones[third], ones[2*third]
	if c+length > len(arr) {
		return []int{-1, -1}
	}
	part1 := arr[a : a+length]
	part2 := arr[b : b+length]
	part3 := arr[c:]
	if len(part3) != length {
		return []int{-1, -1}
	}
	for i := 0; i < length; i++ {
		if part1[i] != part2[i] || part1[i] != part3[i] {
			return []int{-1, -1}
		}
	}
	return []int{a + length - 1, b + length}
}
