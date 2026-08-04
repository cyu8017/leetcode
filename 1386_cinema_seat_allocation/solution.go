// LeetCode 1386 - Cinema Seat Allocation
// https://leetcode.com/problems/cinema-seat-allocation/

func maxNumberOfFamilies(n int, reservedSeats [][]int) int {
	rows := map[int]int{}
	for _, seat := range reservedSeats {
		r, c := seat[0], seat[1]
		if c >= 2 && c <= 9 {
			rows[r] |= 1 << (c - 2)
		}
	}
	ans := 2 * (n - len(rows))
	for _, m := range rows {
		left := m&0b00001111 == 0
		right := m&0b11110000 == 0
		middle := m&0b00111100 == 0
		if left && right {
			ans += 2
		} else if left || right || middle {
			ans++
		}
	}
	return ans
}
