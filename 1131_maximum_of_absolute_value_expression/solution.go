// LeetCode 1131 - Maximum of Absolute Value Expression
// https://leetcode.com/problems/maximum-of-absolute-value-expression/

func maxAbsValExpr(arr1 []int, arr2 []int) int {
	n := len(arr1)
	ans := 0
	signs := [][2]int{{1, 1}, {1, -1}, {-1, 1}, {-1, -1}}
	for _, s := range signs {
		maxV, minV := arr1[0]*s[0]+arr2[0]*s[1]+0, arr1[0]*s[0]+arr2[0]*s[1]+0
		for i := 1; i < n; i++ {
			v := arr1[i]*s[0] + arr2[i]*s[1] + i
			if v > maxV {
				maxV = v
			}
			if v < minV {
				minV = v
			}
		}
		if maxV-minV > ans {
			ans = maxV - minV
		}
	}
	return ans
}
