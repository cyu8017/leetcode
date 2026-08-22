// LeetCode 3453 - Separate Squares I
// https://leetcode.com/problems/separate-squares-i/

func separateSquares(squares [][]int) float64 {
	// binary search horizontal line y
	okArea := func(y float64) float64 {
		var below float64
		for _, sq := range squares {
			yi, l := float64(sq[1]), float64(sq[2])
			top := yi + l
			if y <= yi {
				continue
			}
			if y >= top {
				below += l * l
			} else {
				below += l * (y - yi)
			}
		}
		return below
	}
	var total float64
	for _, sq := range squares {
		l := float64(sq[2])
		total += l * l
	}
	lo, hi := 0.0, 2e9
	for it := 0; it < 60; it++ {
		mid := (lo + hi) / 2
		if okArea(mid)*2 < total {
			lo = mid
		} else {
			hi = mid
		}
	}
	return hi
}
