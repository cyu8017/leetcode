// LeetCode 3609 - Minimum Moves to Reach Target in Grid
// https://leetcode.com/problems/minimum-moves-to-reach-target-in-grid/

impl Solution {
    pub fn min_moves(sx: i32, sy: i32, mut tx: i32, mut ty: i32) -> i32 {
        let mut ans = 0;
        while tx > sx || ty > sy {
            if tx < sx || ty < sy {
                return -1;
            }
            if tx == ty {
                return -1;
            }
            if tx > ty {
                if ty > sy {
                    if tx >= 2 * ty {
                        if tx % 2 != 0 {
                            return -1;
                        }
                        tx /= 2;
                    } else {
                        tx -= ty;
                    }
                    ans += 1;
                } else {
                    if ty != sy {
                        return -1;
                    }
                    while tx > sx {
                        if tx >= 2 * ty {
                            if tx % 2 != 0 {
                                return -1;
                            }
                            tx /= 2;
                        } else {
                            tx -= ty;
                        }
                        ans += 1;
                        if tx < sx {
                            return -1;
                        }
                    }
                }
            } else if tx > sx {
                if ty >= 2 * tx {
                    if ty % 2 != 0 {
                        return -1;
                    }
                    ty /= 2;
                } else {
                    ty -= tx;
                }
                ans += 1;
            } else {
                if tx != sx {
                    return -1;
                }
                while ty > sy {
                    if ty >= 2 * tx {
                        if ty % 2 != 0 {
                            return -1;
                        }
                        ty /= 2;
                    } else {
                        ty -= tx;
                    }
                    ans += 1;
                    if ty < sy {
                        return -1;
                    }
                }
            }
        }
        if tx == sx && ty == sy {
            ans
        } else {
            -1
        }
    }
}
