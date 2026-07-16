// LeetCode 0130 - Surrounded Regions
// https://leetcode.com/problems/surrounded-regions/

func solve(board [][]byte) {
    if len(board)==0 || len(board[0])==0{return}; rows,cols:=len(board),len(board[0])
    var mark func(int,int);mark=func(r,c int){if r<0||r==rows||c<0||c==cols||board[r][c]!='O'{return};board[r][c]='E';mark(r+1,c);mark(r-1,c);mark(r,c+1);mark(r,c-1)}
    for r:=0;r<rows;r++{mark(r,0);mark(r,cols-1)};for c:=0;c<cols;c++{mark(0,c);mark(rows-1,c)}
    for r:=range board{for c:=range board[r]{if board[r][c]=='O'{board[r][c]='X'}else if board[r][c]=='E'{board[r][c]='O'}}}
}