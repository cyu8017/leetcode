// LeetCode 0470 - Implement Rand10() Using Rand7()
// https://leetcode.com/problems/implement-rand10-using-rand7/

func rand7() int {
	panic("rand7 must be provided by the test harness")
}

type Solution struct{}

func (s *Solution) rand10() int {
	for {
		num := (rand7()-1)*7 + rand7()
		if num <= 40 {
			return (num-1)%10 + 1
		}
	}
}
