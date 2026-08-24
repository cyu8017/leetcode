# LeetCode 0690 - Employee Importance
# https://leetcode.com/problems/employee-importance/

class Employee
  attr_accessor :id, :importance, :subordinates

  def initialize(id, importance, subordinates)
    @id = id
    @importance = importance
    @subordinates = subordinates
  end
end

# @param {Employee[]} employees
# @param {Integer} id
# @return {Integer}
def get_importance(employees, id)
  table = {}
  employees.each do |emp|
    if emp.is_a?(Array)
      eid, importance, subordinates = emp
    else
      eid = emp.id
      importance = emp.importance
      subordinates = emp.subordinates
    end
    table[eid] = [importance, subordinates]
  end

  dfs = lambda do |eid|
    importance, subordinates = table[eid]
    importance + subordinates.sum { |sub| dfs.call(sub) }
  end

  dfs.call(id)
end
