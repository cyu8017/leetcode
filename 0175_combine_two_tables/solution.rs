// LeetCode 0175 - Combine Two Tables
// https://leetcode.com/problems/combine-two-tables/

const QUERY: &str = r#"
SELECT
    Person.firstName,
    Person.lastName,
    Address.city,
    Address.state
FROM Person
LEFT JOIN Address
    ON Person.personId = Address.personId
"#;