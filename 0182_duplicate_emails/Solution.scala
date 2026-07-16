object Solution {
  final val QUERY: String = """
SELECT email AS Email
FROM Person
GROUP BY email
HAVING COUNT(*) > 1
"""
}
