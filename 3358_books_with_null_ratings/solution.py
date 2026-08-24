# LeetCode 3358 - Books with NULL Ratings
# https:# leetcode.com/problems/books-with-null-ratings/

# Write your MySQL query statement below
QUERY = """
SELECT book_id, title, author, published_year
FROM books
WHERE rating IS NULL
ORDER BY 1;
"""
