// LeetCode 2019 - The Score of Students Solving Math Expression
// https://leetcode.com/problems/the-score-of-students-solving-math-expression/

func scoreOfStudents(s string, answers []int) int {
	n := len(s)
	correct := evalCorrect2019(s)
	dp := make([][]map[int]bool, n)
	for i := range dp {
		dp[i] = make([]map[int]bool, n)
	}
	var dfs func(l, r int) map[int]bool
	dfs = func(l, r int) map[int]bool {
		if dp[l][r] != nil {
			return dp[l][r]
		}
		res := map[int]bool{}
		if l == r {
			res[int(s[l]-'0')] = true
			dp[l][r] = res
			return res
		}
		for i := l + 1; i < r; i += 2 {
			left := dfs(l, i-1)
			right := dfs(i+1, r)
			for a := range left {
				for b := range right {
					var v int
					if s[i] == '+' {
						v = a + b
					} else {
						v = a * b
					}
					if v <= 1000 {
						res[v] = true
					}
				}
			}
		}
		dp[l][r] = res
		return res
	}
	possible := dfs(0, n-1)
	ans := 0
	for _, a := range answers {
		if a == correct {
			ans += 5
		} else if possible[a] {
			ans += 2
		}
	}
	return ans
}

func evalCorrect2019(s string) int {
	nums := []int{}
	ops := []byte{}
	for i := 0; i < len(s); i++ {
		if s[i] >= '0' && s[i] <= '9' {
			nums = append(nums, int(s[i]-'0'))
		} else {
			ops = append(ops, s[i])
		}
	}
	newNums := []int{nums[0]}
	newOps := []byte{}
	for j, op := range ops {
		if op == '*' {
			newNums[len(newNums)-1] *= nums[j+1]
		} else {
			newOps = append(newOps, op)
			newNums = append(newNums, nums[j+1])
		}
	}
	res := newNums[0]
	for j := range newOps {
		res += newNums[j+1]
	}
	return res
}
