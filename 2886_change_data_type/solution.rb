# LeetCode 2886 - Change Data Type
# https://leetcode.com/problems/change-data-type/

# @param {Object[]} students
# @return {Object[]}
def change_datatype(students)
  students.map do |r|
    if r.is_a?(Array)
      [r[0], r[1], r[2], r[3].to_i]
    else
      row = r.dup
      row["grade"] = r["grade"].to_i
      row
    end
  end
end
