# LeetCode 2230 - The Users That Are Eligible for Discount
# https://leetcode.com/problems/the-users-that-are-eligible-for-discount/

QUERY = <<~SQL
  CREATE PROCEDURE getUserIDs(startDate DATE, endDate DATE, minAmount INT)
  BEGIN
    SELECT DISTINCT user_id
    FROM Purchases
    WHERE time_stamp BETWEEN startDate AND endDate
      AND amount >= minAmount
    ORDER BY user_id;
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
