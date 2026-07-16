// LeetCode 0130 - Surrounded Regions
// https://leetcode.com/problems/surrounded-regions/

impl Solution {
    fn mark(board:&mut Vec<Vec<char>>,row:isize,col:isize){if row<0||col<0||row as usize==board.len()||col as usize==board[0].len()||board[row as usize][col as usize]!='O'{return}board[row as usize][col as usize]='E';Self::mark(board,row+1,col);Self::mark(board,row-1,col);Self::mark(board,row,col+1);Self::mark(board,row,col-1);}
    pub fn solve(board: &mut Vec<Vec<char>>) { if board.is_empty()||board[0].is_empty(){return}let(rows,cols)=(board.len(),board[0].len());for row in 0..rows{Self::mark(board,row as isize,0);Self::mark(board,row as isize,cols as isize-1);}for col in 0..cols{Self::mark(board,0,col as isize);Self::mark(board,rows as isize-1,col as isize);}for row in board.iter_mut(){for cell in row.iter_mut(){*cell=match *cell{'O'=>'X','E'=>'O',other=>other};}}}
}