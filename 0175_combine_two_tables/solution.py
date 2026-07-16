# LeetCode 0175 - Combine Two Tables
# https://leetcode.com/problems/combine-two-tables/

# Write your MySQL query statement below
QUERY = """
SELECT
    Person.firstName,
    Person.lastName,
    Address.city,
    Address.state
FROM Person
LEFT JOIN Address
    ON Person.personId = Address.personId
"""
