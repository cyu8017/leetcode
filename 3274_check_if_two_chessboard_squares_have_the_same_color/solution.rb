# LeetCode 3274 - Check if Two Chessboard Squares Have the Same Color
# https://leetcode.com/problems/check-if-two-chessboard-squares-have-the-same-color/

# @param {String} coordinate1
# @param {String} coordinate2
# @return {Boolean}
def check_two_chessboards(coordinate1, coordinate2)
  c1 = (coordinate1[0].ord - 97) + (coordinate1[1].ord - 49)
  c2 = (coordinate2[0].ord - 97) + (coordinate2[1].ord - 49)
  c1 % 2 == c2 % 2
end
