# LeetCode 2881 - Create a New Column
# https://leetcode.com/problems/create-a-new-column/

# @param {Object[]} employees
# @return {Object[]}
def create_bonus_column(employees)
  employees.map do |r|
    if r.is_a?(Array)
      { "name" => r[0], "salary" => r[1], "bonus" => r[1] * 2 }
    else
      row = r.dup
      row["bonus"] = r["salary"] * 2
      row
    end
  end
end
