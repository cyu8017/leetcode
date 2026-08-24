// LeetCode 2480 - Form A Chemical Bond
// https://leetcode.com/problems/form-a-chemical-bond/

export const QUERY = `SELECT a.symbol AS metal, b.symbol AS nonmetal
FROM
    Elements AS a,
    Elements AS b
WHERE a.type = 'Metal' AND b.type = 'Nonmetal'`;
