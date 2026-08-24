// LeetCode 0780 - Reaching Points
// https://leetcode.com/problems/reaching-points/

impl Solution {
    pub fn reaching_points(sx: i32, sy: i32, mut tx: i32, mut ty: i32) -> bool {
        while tx >= sx && ty >= sy {
            if tx == sx && ty == sy {
                return true;
            }
            if tx == ty {
                break;
            }
            if tx > ty {
                if ty > sy {
                    tx %= ty;
                } else {
                    return (tx - sx) % ty == 0;
                }
            } else if tx > sx {
                ty %= tx;
            } else {
                return (ty - sy) % tx == 0;
            }
        }
        tx == sx && ty == sy
    }
}
