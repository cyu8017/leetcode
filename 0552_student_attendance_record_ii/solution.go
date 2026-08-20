// LeetCode 0552 - Student Attendance Record II
// https://leetcode.com/problems/student-attendance-record-ii/

func checkRecord(n int) int {
	const mod = 1000000007
	dp := [2][3]int{}
	dp[0][0] = 1

	for i := 0; i < n; i++ {
		var nxt [2][3]int
		for absences := 0; absences < 2; absences++ {
			for lates := 0; lates < 3; lates++ {
				ways := dp[absences][lates]
				if ways == 0 {
					continue
				}
				nxt[absences][0] = (nxt[absences][0] + ways) % mod
				if absences == 0 {
					nxt[1][0] = (nxt[1][0] + ways) % mod
				}
				if lates < 2 {
					nxt[absences][lates+1] = (nxt[absences][lates+1] + ways) % mod
				}
			}
		}
		dp = nxt
	}

	total := 0
	for absences := 0; absences < 2; absences++ {
		for lates := 0; lates < 3; lates++ {
			total = (total + dp[absences][lates]) % mod
		}
	}
	return total
}
