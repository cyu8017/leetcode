# How We Solve Find Duplicate File in System

Group file paths by content and keep groups with more than one path.

## Steps

1. Parse each directory entry into path/content pairs.
2. Map content strings to lists of full file paths.
3. Return only groups that contain duplicates.
