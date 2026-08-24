# LeetCode 3246 - Premier League Table Ranking
# https:# leetcode.com/problems/premier-league-table-ranking/

# Write your MySQL query statement below
QUERY = """
SELECT
    team_id,
    team_name,
    wins * 3 + draws points,
    RANK() OVER (ORDER BY (wins * 3 + draws) DESC) position
FROM TeamStats
ORDER BY 3 DESC, 2;
"""
