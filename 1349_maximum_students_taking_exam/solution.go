// LeetCode 1349 - Maximum Students Taking Exam
// https://leetcode.com/problems/maximum-students-taking-exam/

func maxStudents(seats [][]byte) int {
	m, n := len(seats), len(seats[0])
	valid := make([]int, m)
	for r := 0; r < m; r++ {
		mask := 0
		for c := 0; c < n; c++ {
			if seats[r][c] == '.' {
				mask |= 1 << c
			}
		}
		valid[r] = mask
	}
	dp := map[int]int{0: 0}
	for r := 0; r < m; r++ {
		nxt := map[int]int{}
		for cur := 0; cur < (1 << n); cur++ {
			if cur&valid[r] != cur {
				continue
			}
			if cur&(cur<<1) != 0 {
				continue
			}
			bits := 0
			for x := cur; x > 0; x &= x - 1 {
				bits++
			}
			for prev, best := range dp {
				if (cur<<1)&prev == 0 && (cur>>1)&prev == 0 {
					if v := best + bits; v > nxt[cur] {
						nxt[cur] = v
					}
				}
			}
		}
		dp = nxt
	}
	ans := 0
	for _, v := range dp {
		if v > ans {
			ans = v
		}
	}
	return ans
}
