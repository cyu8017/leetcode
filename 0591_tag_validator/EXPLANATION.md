# How We Solve Tag Validator

Scan with a stack: parse CDATA blocks, push start tags, and match end tags.

## Steps

1. On `<![CDATA[`, skip through the next `]]>` (only allowed inside an open tag).
2. On a start tag, validate the uppercase name and push it.
3. On an end tag, pop and match; reject anything after the root closes.
