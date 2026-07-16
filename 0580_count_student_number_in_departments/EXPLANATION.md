# How We Solve Count Student Number in Departments

Left-join students onto departments so empty departments still appear with zero.

## Steps

1. Left join `Department` to `Student` on `dept_id`.
2. Count students per department.
3. Order by student count descending, then department name.
