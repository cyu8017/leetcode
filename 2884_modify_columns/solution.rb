# LeetCode 2884 - Modify Columns
# https://leetcode.com/problems/modify-columns/

# @param {Object[]} employees
# @return {Object[]}
def modify_salary_column(employees)
  employees.map do |r|
    if r.is_a?(Array)
      [r[0], r[1] * 2]
    else
      row = r.dup
      row["salary"] = r["salary"] * 2
      row
    end
  end
end
