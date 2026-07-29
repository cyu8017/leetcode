<?php
// LeetCode 0196 - Delete Duplicate Emails
// https://leetcode.com/problems/delete-duplicate-emails/

const QUERY = <<<'SQL'
DELETE p1
FROM Person p1
JOIN Person p2
  ON p1.email = p2.email
 AND p1.id > p2.id
SQL;
