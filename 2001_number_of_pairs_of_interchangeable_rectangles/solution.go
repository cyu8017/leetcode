// LeetCode 2001 - Number of Pairs of Interchangeable Rectangles
// https://leetcode.com/problems/number-of-pairs-of-interchangeable-rectangles/

func interchangeableRectangles(rectangles [][]int) int64 {
	gcd := func(a, b int) int {
		for b != 0 {
			a, b = b, a%b
		}
		return a
	}
	freq := map[[2]int]int{}
	var ans int64
	for _, rect := range rectangles {
		w, h := rect[0], rect[1]
		g := gcd(w, h)
		key := [2]int{w / g, h / g}
		ans += int64(freq[key])
		freq[key]++
	}
	return ans
}
