// LeetCode 1853 - Convert Date Format
// https://leetcode.com/problems/convert-date-format/

export const QUERY = `SELECT DATE_FORMAT(day, '%W, %M %e, %Y') AS day
FROM Days
`;
