# How We Solve Accounts Merge

Union emails that appear in the same account, then group by root email.

## Steps

1. Union-find over every email; remember each email’s display name.
2. Collect emails by their parent root.
3. Emit `[name] + sorted(emails)` for each component.
