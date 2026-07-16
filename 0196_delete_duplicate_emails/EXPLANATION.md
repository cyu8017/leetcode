# How We Solve Delete Duplicate Emails

Delete higher-id rows that share an email with a lower-id row.

## Steps

1. Self-join `Person` on matching email.
2. Keep pairs where the left id is greater.
3. Delete those left-side duplicates.
4. The smallest id for each email remains.
5. The table now has unique emails.
