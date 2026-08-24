// LeetCode 2205 - The Number Of Users That Are Eligible For Discount
// https://leetcode.com/problems/the-number-of-users-that-are-eligible-for-discount/

export const QUERY = `CREATE FUNCTION getUserIDs(startDate DATE, endDate DATE, minAmount INT) RETURNS INT
READS SQL DATA
BEGIN
  RETURN (
    SELECT COUNT(DISTINCT user_id) AS user_cnt
    FROM Purchases
    WHERE time_stamp BETWEEN startDate AND endDate
      AND amount >= minAmount
  );
END`;
