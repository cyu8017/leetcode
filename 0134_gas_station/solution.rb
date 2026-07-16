class Solution
  def can_complete_circuit(gas, cost)
    total = 0
    tank = 0
    start = 0

    gas.each_index do |i|
      difference = gas[i] - cost[i]
      total += difference
      tank += difference
      if tank.negative?
        start = i + 1
        tank = 0
      end
    end
    total >= 0 ? start : -1
  end
end