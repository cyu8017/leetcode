// LeetCode 3265 - Count Almost Equal Pairs I
// https://leetcode.com/problems/count-almost-equal-pairs-i/

func countPairs(nums []int) int {
	ans := 0
	for i := 0; i < len(nums); i++ {
		for j := i + 1; j < len(nums); j++ {
			if almostEqual3265(nums[i], nums[j]) {
				ans++
			}
		}
	}
	return ans
}

func almostEqual3265(a, b int) bool {
	sa := sprintfNum(a)
	sb := sprintfNum(b)
	for len(sa) < len(sb) {
		sa = "0" + sa
	}
	for len(sb) < len(sa) {
		sb = "0" + sb
	}
	diff := []int{}
	for i := 0; i < len(sa); i++ {
		if sa[i] != sb[i] {
			diff = append(diff, i)
		}
	}
	if len(diff) == 0 {
		return true
	}
	if len(diff) != 2 {
		return false
	}
	i, j := diff[0], diff[1]
	return sa[i] == sb[j] && sa[j] == sb[i]
}

func sprintfNum(x int) string {
	if x == 0 {
		return "0"
	}
	var b []byte
	for x > 0 {
		b = append([]byte{byte('0' + x%10)}, b...)
		x /= 10
	}
	return string(b)
}
