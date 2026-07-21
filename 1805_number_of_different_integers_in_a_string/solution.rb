
# @param {String} word
# @return {Integer}
def num_different_integers(word)
  seen = {}
  word.scan(/\d+/).each { |m| seen[m.to_i] = true }
  seen.length
end
