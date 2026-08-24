# LeetCode 2880 - Select Data
# https://leetcode.com/problems/select-data/

# @param {Object[]} students
# @return {Object[]}
def select_data(students)
  out = []
  students.each do |r|
    sid = r.is_a?(Array) ? r[0] : r["student_id"]
    next unless sid == 101

    if r.is_a?(Array)
      out << { "name" => r[1], "age" => r[2] }
    else
      out << { "name" => r["name"], "age" => r["age"] }
    end
  end
  out
end
