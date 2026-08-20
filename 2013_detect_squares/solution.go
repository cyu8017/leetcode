// LeetCode 2013 - Detect Squares
// https://leetcode.com/problems/detect-squares/

type DetectSquares struct {
	cnt map[[2]int]int
}

func Constructor() DetectSquares {
	return DetectSquares{cnt: map[[2]int]int{}}
}

func (this *DetectSquares) Add(point []int) {
	key := [2]int{point[0], point[1]}
	this.cnt[key]++
}

func (this *DetectSquares) Count(point []int) int {
	x, y := point[0], point[1]
	ans := 0
	for p, c := range this.cnt {
		px, py := p[0], p[1]
		if px == x || py == y {
			continue
		}
		if abs2013(px-x) != abs2013(py-y) {
			continue
		}
		ans += c * this.cnt[[2]int{px, y}] * this.cnt[[2]int{x, py}]
	}
	return ans
}

func abs2013(x int) int {
	if x < 0 {
		return -x
	}
	return x
}
