// LeetCode 3391 - Design a 3D Binary Matrix with Efficient Layer Tracking
// https://leetcode.com/problems/design-a-3d-binary-matrix-with-efficient-layer-tracking/

type Matrix3D struct {
	m    [][][]int
	ones []int
	n    int
}

func Constructor(n int) Matrix3D {
	m := make([][][]int, n)
	for i := range m {
		m[i] = make([][]int, n)
		for j := range m[i] {
			m[i][j] = make([]int, n)
		}
	}
	return Matrix3D{m: m, ones: make([]int, n), n: n}
}

func (this *Matrix3D) SetCell(x int, y int, z int) {
	if this.m[x][y][z] == 0 {
		this.m[x][y][z] = 1
		this.ones[x]++
	}
}

func (this *Matrix3D) UnsetCell(x int, y int, z int) {
	if this.m[x][y][z] == 1 {
		this.m[x][y][z] = 0
		this.ones[x]--
	}
}

func (this *Matrix3D) LargestMatrix() int {
	best, idx := -1, 0
	for i := 0; i < this.n; i++ {
		if this.ones[i] >= best {
			best = this.ones[i]
			idx = i
		}
	}
	return idx
}
