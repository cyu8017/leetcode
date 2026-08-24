# LeetCode 2205 - The Number of Users That Are Eligible for Discount
# https://leetcode.com/problems/the-number-of-users-that-are-eligible-for-discount/

QUERY = <<~SQL
  CREATE FUNCTION getUserIDs(startDate DATE, endDate DATE, minAmount INT) RETURNS INT
  READS SQL DATA
  BEGIN
    RETURN (
      SELECT COUNT(DISTINCT user_id) AS user_cnt
      FROM Purchases
      WHERE time_stamp BETWEEN startDate AND endDate
        AND amount >= minAmount
    );
  END
SQL

# @param {Object} start_date
# @param {Object} end_date
# @param {Integer} min_amount
# @return {Object}
def get_user_ids(*_args)
  QUERY
end

alias solve get_user_ids
