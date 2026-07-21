
# @param {Integer[]} sensor1
# @param {Integer[]} sensor2
# @return {Integer}
def bad_sensor(sensor1, sensor2)
  return -1 if sensor1 == sensor2

  is_defective = lambda do |correct, faulty|
    n = correct.length
    i = 0
    i += 1 while i < n && correct[i] == faulty[i]
    return false if i == n

    j = i
    j += 1 while j < n - 1 && correct[j + 1] == faulty[j]
    j == n - 1
  end

  sensor1_bad = is_defective.call(sensor2, sensor1)
  sensor2_bad = is_defective.call(sensor1, sensor2)

  return -1 if sensor1_bad && sensor2_bad
  return 1 if sensor1_bad
  return 2 if sensor2_bad
  -1
end
