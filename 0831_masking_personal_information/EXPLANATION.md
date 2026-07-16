# How We Solve Masking Personal Information

Branch on email vs phone and apply the fixed mask templates.

## Steps

1. Email: lowercase, keep first/last of name, insert five `*`.
2. Phone: keep digits only; last 4 form `XXXX`.
3. Prefix country-code stars by digit count beyond 10.
