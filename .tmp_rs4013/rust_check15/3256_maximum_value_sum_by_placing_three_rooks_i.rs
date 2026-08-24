struct Solution;
// LeetCode 3256 - Maximum Value Sum by Placing Three Rooks I
// https://leetcode.com/problems/maximum-value-sum-by-placing-three-rooks-i/

impl Solution {
    pub fn maximum_value_sum(board: Vec<Vec<i32>>) -> i64 {
        let m = board.len();
        let n = board[0].len();
        let mut tops: Vec<Vec<(i32, usize)>> = Vec::new();
        for i in 0..m {
            let mut row: Vec<(i32, usize)> = Vec::new();
            for j in 0..n {
                let cur = (board[i][j], j);
                let mut placed = false;
                for t in 0..row.len() {
                    if cur.0 > row[t].0 {
                        row.insert(t, cur);
                        placed = true;
                        break;
                    }
                }
                if !placed {
                    row.push(cur);
                }
                if row.len() > 3 {
                    row.truncate(3);
                }
            }
            tops.push(row);
        }
        let mut ans = i64::MIN / 2;
        for i in 0..m {
            for &(av, ac) in &tops[i] {
                for j in i + 1..m {
                    for &(bv, bc) in &tops[j] {
                        if ac == bc {
                            continue;
                        }
                        for k in j + 1..m {
                            for &(cv, cc) in &tops[k] {
                                if cc == ac || cc == bc {
                                    continue;
                                }
                                let s = av as i64 + bv as i64 + cv as i64;
                                if s > ans {
                                    ans = s;
                                }
                            }
                        }
                    }
                }
            }
        }
        ans
    }
}

fn main() {}
