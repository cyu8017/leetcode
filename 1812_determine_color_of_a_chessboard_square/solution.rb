
# @param {String} coordinates
# @return {Boolean}
def square_is_white(coordinates)
  col = coordinates[0].ord - 'a'.ord + 1
  row = coordinates[1].to_i
  (col + row).odd?
end
