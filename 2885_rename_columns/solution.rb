# LeetCode 2885 - Rename Columns
# https://leetcode.com/problems/rename-columns/

# @param {Object[]} students
# @return {Object[]}
def rename_columns(students)
  students.map do |r|
    if r.is_a?(Array)
      {
        "student_id" => r[0],
        "first_name" => r[1],
        "last_name" => r[2],
        "age_in_years" => r[3]
      }
    else
      {
        "student_id" => r["id"],
        "first_name" => r["first"],
        "last_name" => r["last"],
        "age_in_years" => r["age"]
      }
    end
  end
end
