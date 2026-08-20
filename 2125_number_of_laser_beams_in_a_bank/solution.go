// LeetCode 2125 - Number of Laser Beams in a Bank
// https://leetcode.com/problems/number-of-laser-beams-in-a-bank/

func numberOfBeams(bank []string) int {
	ans, prev := 0, 0
	for _, row := range bank {
		cnt := 0
		for i := 0; i < len(row); i++ {
			if row[i] == '1' {
				cnt++
			}
		}
		if cnt > 0 {
			ans += prev * cnt
			prev = cnt
		}
	}
	return ans
}
