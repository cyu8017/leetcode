# LeetCode 2883 - Drop Missing Data
# https://leetcode.com/problems/drop-missing-data/

# @param {Object[]} students
# @return {Object[]}
def drop_missing_data(students)
  out = []
  students.each do |r|
    name = r.is_a?(Array) ? r[1] : r["name"]
    out << r if !name.nil? && name != ""
  end
  out
end
