// LeetCode 3274 - Check if Two Chessboard Squares Have the Same Color
// https://leetcode.com/problems/check-if-two-chessboard-squares-have-the-same-color/

func checkTwoChessboards(coordinate1 string, coordinate2 string) bool {
	c1 := int(coordinate1[0]-'a') + int(coordinate1[1]-'1')
	c2 := int(coordinate2[0]-'a') + int(coordinate2[1]-'1')
	return c1%2 == c2%2
}
