# LeetCode 1683 - Invalid Tweets
# https://leetcode.com/problems/invalid-tweets/

QUERY = <<~SQL
  SELECT tweet_id FROM Tweets WHERE CHAR_LENGTH(content)>15
SQL
