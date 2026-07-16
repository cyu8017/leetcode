def get_row(row_index)
  row = [1]
  1.upto(row_index) do |size|
    row << 1
    (size - 1).downto(1) do |index|
      row[index] += row[index - 1]
    end
  end
  row
end