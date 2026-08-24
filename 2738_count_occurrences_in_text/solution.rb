# LeetCode 2738 - Count Occurrences in Text
# https:# leetcode.com/problems/count-occurrences-in-text/

QUERY = <<~SQL
  SELECT 'bull' AS word, COUNT(*) AS count
  FROM Files
  WHERE content LIKE '% bull %'
  UNION
  SELECT 'bear' AS word, COUNT(*) AS count
  FROM Files
  WHERE content LIKE '% bear %'
SQL
