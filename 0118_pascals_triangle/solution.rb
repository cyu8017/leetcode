def generate(num_rows)
  result = []
  num_rows.times do |row_index|
    row = Array.new(row_index + 1, 1)
    (1...row_index).each do |index|
      row[index] = result[-1][index - 1] + result[-1][index]
    end
    result << row
  end
  result
end