<?php
// LeetCode 1517 - Find Users With Valid E-Mails
// https://leetcode.com/problems/find-users-with-valid-e-mails/

const QUERY = <<<'SQL'
SELECT user_id, name, mail
FROM Users
WHERE mail REGEXP '^[A-Za-z][A-Za-z0-9_.-]*@leetcode[.]com$'
SQL;
