// LeetCode 2643 - Row With Maximum Ones
// https://leetcode.com/problems/row-with-maximum-ones/

export function rowAndMaximumOnes(mat: any): any {
    let bestRow = 0, bestCnt = -1;
    for (let i = 0; i < mat.length; i++) {
        let cnt = 0;
        for (const v of mat[i]) cnt += v;
        if (cnt > bestCnt) { bestCnt = cnt; bestRow = i; }
    }
    return [bestRow, bestCnt];
}
